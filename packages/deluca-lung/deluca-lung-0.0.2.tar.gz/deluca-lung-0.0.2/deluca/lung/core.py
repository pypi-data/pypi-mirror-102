import os
import torch
import dill as pickle


class VentObj(torch.nn.Module):
    def __new__(cls, *args, **kwargs):
        obj = object.__new__(cls)
        obj.__setattr__("name", cls.__name__)
        torch.nn.Module.__init__(obj)
        return obj

    def kwargs(self, **kwargs):
        for kw, arg in kwargs.items():
            self.__setattr__(kw, arg)

    def save(self, path, thing=None):
        obj = thing or self
        dirname = os.path.abspath(os.path.dirname(path))
        if not os.path.exists(dirname):
            os.makedirs(dirname)

        pickle.dump(obj, open(path, "wb"))

    def tensor(self, val, requires_grad=True, dtype=None, device="cpu"):
        if dtype is None:
            dtype = torch.get_default_dtype()
        return torch.tensor(val, requires_grad=requires_grad, dtype=dtype, device=device)

    @classmethod
    def load(cls, path):
        return pickle.load(open(path, "rb"))
