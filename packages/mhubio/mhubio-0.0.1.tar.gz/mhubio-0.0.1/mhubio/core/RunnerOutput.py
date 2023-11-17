from enum import Enum
from typing import Type, Any, List, Optional, Union, Dict
from .Meta import Meta

class RunnerOutputType(Enum):
    ValuePrediction = 'ValuePrediction'
    ClassPrediction = 'ClassPrediction'
    DictPrediction = 'DictPrediction'
    ListPrediction = 'ListPrediction'

class RunnerOutput(): # Outcome?

    name: str
    label: str
    description: str
    type: RunnerOutputType
    _meta: Optional[Meta]

    def __str__(self):
        return f"[O:{self.name}:{self.type}:{self.label}:{self.description}]"

    @property # use property for optional values assigned via decorator
    def meta(self) -> Optional[Meta]:
        if hasattr(self, '_meta'):
            return self._meta
        return None
    
    @meta.setter
    def meta(self, meta: Optional[Meta]):
        self._meta = meta

    # static decorator function that assigns meta
    @staticmethod
    def Meta(meta: Meta):
        def decorator(cls):
            cls.meta = meta
            return cls
        return decorator

    # static decorator function that assigns name
    @staticmethod
    def Name(name: str):
        def decorator(cls):
            cls.name = name
            return cls
        return decorator
    
    # static decorator function that assigns label
    @staticmethod
    def Label(label: str):
        def decorator(cls):
            cls.label = label
            return cls
        return decorator
    
    # static decorator function that assigns description
    @staticmethod
    def Description(description: str):
        def decorator(cls):
            cls.description = description
            return cls
        return decorator
    
class ValueOutput(RunnerOutput):

    dtype: Type
    _value: Optional[Any]

    def __init__(self):
        super().__init__()
        self.type = RunnerOutputType.ValuePrediction

    @property
    def value(self) -> Optional[Any]:
        assert self._value is None or isinstance(self._value, self.dtype), f"Value {self._value} is not of type {self.dtype}."
        return self._value
    
    @value.setter
    def value(self, value: Optional[Any]):
        assert value is None or isinstance(value, self.dtype), f"Value {value} is not of type {self.dtype}."
        self._value = value

    # static decorator function that assigns type
    @staticmethod
    def Type(dtype: Type):
        def decorator(cls):
            cls.dtype = dtype
            return cls
        return decorator
    
    def __str__(self):
        return super().__str__() + f"({self.value})"

class OutputClass():
    classID: Union[int, str]
    probability: Optional[float] = None
    label: str
    description: str

    def __init__(self, classID: Union[int, str], label: str, description: str):
        self.classID = classID
        self.label = label
        self.description = description

    def __str__(self):
        return f"[C:{self.classID}:{self.label}]({self.probability})"

class ClassOutput(RunnerOutput):

    classes: List[OutputClass]
    _classID: Optional[Union[str, int]]

    def __init__(self) -> None:
        super().__init__()
        self.type = RunnerOutputType.ClassPrediction

        # reverse classes list, so top most decorator has index 0
        if hasattr(self, 'classes') and isinstance(self.classes, list):
            self.classes.reverse() 

    @property
    def value(self) -> Optional[Union[str, int]]:
        return self._classID
    
    @value.setter
    def value(self, classID: Optional[Union[str, int]]):
        assert classID is None or classID in self, f"Class with ID {classID} not found."
        self._classID = classID

    @property
    def predictedClass(self) -> Optional[OutputClass]:
        return self[self.value] if self.value is not None else None

    def assign_probabilities(self, class_data: Union[List[float], Dict[Union[str, int], float]]):
        """ Assigns probabilities to classes.
        
            class_data can be either a list of probabilities in the order as classes are defined 
            or a dictionary with classIDs as keys and the probabilities as float values.

            Note: decorators are read from top to bottom. 
                We therefore reverse the classes list, 
                so the top most decorator has index 0.
        """
        if isinstance(class_data, dict):
            for classID, probability in class_data.items():
                self[classID].probability = probability
        elif isinstance(class_data, list):
            for i, probability in enumerate(class_data):
                self.classes[i].probability = probability

    # access classes by their classID
    def __getitem__(self, classID: Union[str, int]) -> OutputClass:
        for c in self.classes:
            if c.classID == classID:
                return c
        raise KeyError(f"Class with ID {classID} not found.")

    # in operator to check if classID is in classes
    def __contains__(self, classID: Union[str, int]) -> bool:
        return any(c.classID == classID for c in self.classes)

    def __str__(self):
        return super().__str__() + f"<{'|'.join(str(c) for c in self.classes)}>({str(self.predictedClass)})"

    # static decorator to define a output class
    @staticmethod
    def Class(classID: Union[int, str], label: str, the: str):
        def decorator(cls):
            if not hasattr(cls, 'classes'):
                cls.classes = []
            cls.classes.append(OutputClass(classID, label, the))
            return cls
        return decorator

class DictOutputItem():
    key: str
    dtype: Type
    description: str
    _value: Optional[Any]

    def __init__(self, key: str, dtype: Type, description: str):
        self.key = key
        self.dtype = dtype
        self.description = description

    @property
    def value(self) -> Any:
        assert self._value is None or isinstance(self._value, self.dtype), f"Value {self._value} is not of type {self.dtype}."
        return self._value
    
    @value.setter
    def value(self, value: Optional[Any]):
        assert value is None or isinstance(value, self.dtype), f"Value {value} is not of type {self.dtype}."
        self._value = value

    def __str__(self):
        return f"[D:{self.key}:{self.dtype}:{self.description}]"

class DictOutput(RunnerOutput):
    items: Dict[str, DictOutputItem]

    def __init__(self, value: Optional[Dict[str, Any]] = None):
        super().__init__()
        self.type = RunnerOutputType.DictPrediction
        self.value = value

    @property
    def value(self) -> Optional[Dict[str, Any]]:
        # NOTE: omitting items with value None (we might need to set this behavior, however, role of .value is unclear for the dict output anyways...)
        return {k: v.value for k, v in self.items.items() if v.value is not None}
    
    @value.setter
    def value(self, value: Optional[Dict[str, Any]]):
        # reset all items if value is None
        if value is None:
            for item in self.items.values():
                item.value = None
            return
        
        # update existing items from dict if value is not None
        assert isinstance(value, dict), f"Value {value} is not a dict nor None."
        for k, v in value.items():
            assert k in self.items, f"Key {k} not found in items."
            assert isinstance(v, self.items[k].dtype), f"Value {v} is not of type {self.items[k].dtype}."
            self.items[k].value = v

    def set(self, key: str, value: Any):
        assert key in self.items, f"Key {key} not found in items."
        assert isinstance(value, self.items[key].dtype), f"Value {value} is not of type {self.items[key].dtype}."
        self.items[key].value = value

    # static decorator function that assigns type
    @staticmethod
    def Item(key: str, dtype: Type, the: str):
        def decorator(cls):
            if not hasattr(cls, 'items'):
                cls.items = {}
            cls.items[key] = DictOutputItem(key, dtype, the)
            return cls
        return decorator
    
    def __str__(self):
        return super().__str__() + f"({self.value})"

class ListOutput(RunnerOutput):

    dtype: Type
    _value: Optional[List[Any]]

    def __init__(self):
        super().__init__()
        self.type = RunnerOutputType.ListPrediction
        self._value = None

    @property
    def value(self) -> Optional[Any]:
        assert self._value is None or (isinstance(self._value, list) and all(isinstance(v, self.dtype) for v in self._value)), \
            f"Value {self._value} is not a list of type {self.dtype}."
        return self._value
    
    @value.setter
    def value(self, value: Optional[List[Any]]):
        assert value is None or (isinstance(value, list) and all(isinstance(v, self.dtype) for v in value)), \
            f"Value {value} is not a list of type {self.dtype}."
        self._value = value

    def add(self, item: Any):
        assert isinstance(item, self.dtype), f"Item {item} is not of type {self.dtype}."
        if self._value is None:
            self._value = []
        self._value.append(item)

    # static decorator function that assigns type
    @staticmethod
    def Type(dtype: Type):
        def decorator(cls):
            cls.dtype = dtype
            return cls
        return decorator
    
    def __str__(self):
        return super().__str__() + f"({[str(x) for x in self.value or []]})"