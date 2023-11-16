"""
1. Patch是对一个或多个mini-batch运行结果的封装，用于batch指标计算、epoch指标计算等。
2. Patch有三个重要方法：
    - new:      返回一个封装了数据、指标等的新对象
    - forward:  无参数，用于计算或处理封装的数据
    - add:      参数为另一个Patch对象，返回一个由两个Patch相加合并而成的新的Patch对象
3. Patch的类型
    - ValuePatch:    new方法关键参数为(mean_value, batch_size)  forward方法返回一个值或字典
    - MetricPatch:   new方法关键参数为(preds, targets)          forward方法返回一个指标值或指标字典
    - MetricFnPatch: new方法关键参数为(metric, preds, targets)  forward方法返回一个指标值或指标字典
4. Trainer中可以指定多个Patch，但最多只能有一个MetricFnPatch
5. 内置Patch
    - PatchBase
        - ValuePatch
            - `patches.ValuePatch`
        - MetricPatch
            - `patches.ConfusionPatch`
        - MetricFnPatch:
            - `patches.TensorPatch`
            - `patches.MeanPatch` （与混淆矩阵相关的指标函数，如accuracy、precision、recall、f1等不能使用MeanPatch）
6. 定制Patch
    - 定制用于计算指标的Patch可继承MetricPatch，实现forward方法和add方法
"""
import abc
import torch
import numpy as np
from typing import Literal
from copy import deepcopy
from .metrics import confusion_matrix, accuracy, precision, recall, fbeta
from .loops import keyset


def run_patch_dict(patch_dict):
    """
    计算一个Patch字典的指标值（计算Batch指标）
    """
    # return {patch_name(k, v): v() for k, v in patch_dict.items()}
    return {k: v() for k, v in patch_dict.items()}


def run_patch_dicts(patch_dicts):
    """
    计算Patch字典的列表的指标值（计算Epoch指标）
    """
    if len(patch_dicts) == 0:
        return None
    return {k: sum(dic[k] for dic in patch_dicts)() for k in keyset(patch_dicts)}


class Patch(abc.ABC):
    """
    所有Patch对象的基类
    """
    def __init__(self, name):
        """
        Args:
            name: 显示在输出日志中的名称
        """
        assert len(name.strip()) > 0, 'Patch的`name`不能为空字符！'
        super().__init__()
        self.name = name

    def __add__(self, obj):
        return self.__add(obj)

    def __radd__(self, obj):
        return self.__add(obj)

    def __add(self, obj):
        if obj == 0:
            return self
        assert isinstance(obj, self.__class__), '相加的两个Patch的类型不一致！'
        return self.add(obj)

    def __call__(self):
        return self.forward()

    @abc.abstractmethod
    def new(self, *args, **kwargs):
        """
        复制自身或创建一个完全相同的对象，将preds、targets等数据封装入该对象，并将其返回。
        例如：
            obj = self.__class__(self.name)
            obj.preds = [preds]
            obj.targets = [targets]
            return obj
        """

    @abc.abstractmethod
    def forward(self):
        """
        基于当前Patch中保存的数据，计算一个结果（如指标值）并返回，被__call__方法自动调用。
        """

    @abc.abstractmethod
    def add(self, obj):
        """
        用于重载“+”运算符，将self和obj两个对象相加，得到一个新的对象。
        注意：在相加之前检查self和obj是否能够相加
        """


class ValuePatch(Patch):
    """
    new 方法:     关键参数为(mean_value, batch_size)
    forward 方法: 返回一个值或字典。
    主要用于根据mini-batch平均损失得到epoch平均损失（也可用于与损失相似的数值的累积平均计算），支持字典值的累积平均计算。

    例如：
        batch 1的平均损失为 loss1, 批量大小为 bsize1；
        batch 2的平均损失为 loss2, 批量大小为 bsize3；
        计算两个batch的平均损失：
            _vp = ValuePatch('loss')
            vp1 = _vp.new(loss1, bsize1)    # 封装了数据的新对象
            vp2 = _vp.new(loss2, bsize2)    # 封装了新数的新对象
            vp = 0 + vp1 + vp2              # 两个Patch直接相加，而且可以与0相加
            vp = sum([vp1, vp2])            # 可利用sum进行运算
            vp1()                           # batch 1上的平均损失
            vp2()                           # batch 2上的平均扣抽
            vp()                            # 两个mini-batch的平均损失
    """

    def new(self, mean_value, batch_size):
        """
        Args:
            mean_value: 一个mini-batch的平均值，例如平均损失；或者多个mini-batch平均值组成的字典。
            batch_size: mini-batch的大小
        """
        obj = self.__class__(self.name)
        if isinstance(mean_value, dict):
            obj.batch_value = {k: v * batch_size for k, v in mean_value.items()}
        else:
            obj.batch_value = mean_value * batch_size
        obj.batch_size = batch_size
        return obj

    def forward(self):
        if isinstance(self.batch_value, dict):
            return {k: v / self.batch_size for k, v in self.batch_value.items()}
        else:
            return self.batch_value / self.batch_size

    def add(self, obj):
        batch_size = self.batch_size + obj.batch_size
        mean_value = add_patch_value(self.batch_value, obj.batch_value, batch_size)
        return self.new(mean_value, batch_size)


def add_patch_value(b_value1, b_value2, b_size=1):
    if isinstance(b_value1, dict):
        assert isinstance(b_value2, dict) and len(b_value1) == len(b_value2), '相加的两个Patch值不匹配！'
        keys1 = b_value1.keys()
        keys2 = b_value2.keys()
        assert len(set(keys1).difference(set(keys2))) == 0, '相加的两个Patch值（字典）的key不一致！'
        batch_value = {k: (b_value1[k]+b_value2[k])/b_size for k in keys1}
    else:
        batch_value = (b_value1 + b_value2)/b_size
    return batch_value



class MetricPatch(Patch):
    """
    new 方法:     关键参数为(preds, targets)
    forward 方法: 返回一个指标值或指标字典
    """


class MetricFnPatch(Patch):
    """
    new 方法:     关键参数为(metric, preds, targets)
    forward 方法: 返回一个指标值或指标字典
    """


class TensorPatch(MetricFnPatch):
    """
    new 方法:     关键参数为(metric, preds, targets)
    forward 方法: 返回一个指标值或指标字典

    用于累积多个mini-batch的preds和targets，计算Epoch的指标。
    例如：
        batch 1的模型预测为preds1, 标签为targets1；
        batch 1的模型预测为preds2, 标签为targets2；
        m_fun 为指标计算函数；
        计算两个batch的指标：
            tp = TensorPatch('metric_name')
            p1 = tp.new(m_fun, preds1, targets1)
            p2 = tp.new(m_fun, preds2, targets2)
            p = 0 + p1 + p2          # 两个Patch可直接相加，而且可与0相加
            p = sum([p1, p2])        # 可利用sum进行运算
            p1()  # batch 1上的指标值
            p2()  # batch 2上的指标值
            p()   # 两个batch上的指标值
    """
    def __init__(self, name='fn_patch'):
        super().__init__(name)

    def new(self, metric, preds, targets, single_batch=True):
        """
        Args:
            metric:       计算指标的函数（或其他适当的可调用对象）
            preds:        模型预测结果
            targets:      标签（当指标计算不需要标签时为空值）
            single_batch: preds, targets中包含的是单个还是多个batch的数据（主要仅用于add函数）
        """
        assert callable(metric), '指标`metric`应当是一个可调用对象！'
        obj = self.__class__(self.name)
        obj.metric = metric
        if single_batch:     # 单个mini-batch的模型预测输出
            obj.preds = [preds] if isinstance(preds, (list, tuple)) else [[preds]]              # 应对模型有多个输出的情况
        else:                # 多个mini-batch模型预测输出
            obj.preds = preds
        if targets is None:
            obj.targets = None
        else:
            if single_batch: # 单个mini-batch的标签数据
                obj.targets = [targets] if isinstance(targets, (list, tuple)) else [[targets]]  # 应对模型有多个标签的情况
            else:            # 多个mini-batch的标签数据
                obj.targets = targets

        obj.concat = torch.concat if isinstance(obj.preds[0][0], torch.Tensor) else np.concatenate
        return obj

    def forward(self):
        preds = [self.concat(prds, 0) for prds in zip(*self.preds)]
        targets = None if self.targets is None else [self.concat(tgts, 0) for tgts in zip(*self.targets)]
        preds = preds[0] if len(preds) == 1 else preds
        targets = targets[0] if len(targets) == 1 else targets
        return self.metric(preds, targets)

    def add(self, obj):
        assert self.metric is obj.metric, '相加的两个Patch的`metric`不一致'
        new_preds = self.preds + obj.preds
        if self.targets != None:
            assert obj.targets is not None, '相加的两个Patch的`batch_targets`其中一个为None！'
            new_targets = self.targets + obj.targets
        else:
            new_targets = None
        return self.new(self.metric, new_preds, new_targets, single_batch=False)


class MeanPatch(MetricFnPatch):
    """
    注意：与混淆矩阵相关的指标函数，如accuracy、precision、recall、f1等不能使用MeanPatch。
         可使用默认的Tensorpatch或者ConfusionPatch。
    """
    def __init__(self, name='fn_patch'):
        super().__init__(name)

    def new(self, metric, preds, targets):
        """
        Args:
            metric: 计算指标的函数（或其他适当的可调用对象），必须返回经过平均指标值。
            batch_pres: 一个mini_batch的模型预测
            batch_targets: 一个mini_batch的标签（当指标计算不需要标签时为空值）
        """
        assert callable(metric), '指标`metric`应当是一个可调用对象！'
        obj = self.__class__(self.name)
        obj.metric = metric
        obj.batch_size = len(preds)
        m_value = metric(preds, targets)
        if isinstance(m_value, dict):
            obj.batch_value = {k: v * obj.batch_size for k, v in m_value.items()}
        else:
            obj.batch_value = m_value * obj.batch_size
        return obj

    def forward(self):
        if isinstance(self.batch_value, dict):
            return {k: v / self.batch_size for k, v in self.batch_value.items()}
        else:
            return self.batch_value / self.batch_size

    def add(self, obj):
        assert self.metric is obj.metric, '相加的两个Patch的`metric`不一致'
        new_obj = deepcopy(self)
        new_obj.batch_value = add_patch_value(self.batch_value, obj.batch_value)
        new_obj.batch_size = self.batch_size + obj.batch_size
        return new_obj


class ConfusionPatch(MetricPatch):
    def __init__(self, name='C.', metrics=('accuracy', 'precision', 'recall', 'f1', 'fbeta'),
                 average: Literal['micro', 'macro', 'weighted']='micro', beta=1.0):
        """
        能够累积计算基于混淆矩阵的指标，包括'accuracy', 'precision', 'recall', 'f1', 'fbeta'等。
        Args:
            name:           显示在输出日志中的名称
            batch_preds:    模型预测
            batch_targets:  标签
            metrics:        需计算的标签，'accuracy', 'precision', 'recall', 'f1', 'fbeta'中的一个或多个
            average:        多分类下的平均方式'micro', 'macro', 'weighted'之一
            beta:           F_beta中的beta
        """
        super().__init__(name)
        if isinstance(metrics, str):
            metrics = [metrics]

        assert set(metrics) <= set(['accuracy', 'precision', 'recall', 'f1', 'fbeta']),\
                "未知`metrics`！可取值为{'accuracy', 'precision', 'recall', 'f1', 'fbeta'}的子集！"
        assert average in ['micro', 'macro', 'weighted'], "`average`取值为['micro', 'macro', 'weighted']之一！"
        self.metric2name = {'accuracy': 'acc', 'recall': 'r', 'precision': 'p', 'f1': 'f1', 'fbeta': 'fb'}

        assert beta > 0, 'F_beta中的beta必须大于0！'
        self.beta = beta

        self.metrics = metrics
        self.average = average

    def new(self, preds, targets):
        obj = self.__class__(self.name, self.metrics, self.average, self.beta)
        if preds.shape[1] == 1:
            num_classes = int((max(targets) + 1).item())
        else:
            num_classes = preds.shape[1]
        obj.num_classes = num_classes
        obj.confusion_matrix = confusion_matrix(preds, targets, num_classes)
        return obj

    def forward(self):
        return {self.metric2name[m]: getattr(self, m)() for m in self.metrics}

    def add(self, obj):
        new_obj = deepcopy(self)
        assert self.confusion_matrix.shape == obj.confusion_matrix.shape, '相加的两个Patch中数据的类别数量不相等！'
        assert set(self.metrics) == set(obj.metrics), '相加的两个Patch的`metrics`不一致!'
        assert self.average == obj.average, '相加的两个Patch的`average`不一致!'
        new_obj.confusion_matrix = self.confusion_matrix + obj.confusion_matrix
        return new_obj

    def accuracy(self):
        return accuracy(conf_mat=self.confusion_matrix)

    def precision(self):
        return precision(average=self.average, conf_mat=self.confusion_matrix)

    def recall(self):
        return recall(average=self.average, conf_mat=self.confusion_matrix)

    def fbeta(self):
        return fbeta(average=self.average, beta=self.beta, conf_mat=self.confusion_matrix)

    def f1(self):
        return fbeta(average=self.average, beta=1, conf_mat=self.confusion_matrix)
