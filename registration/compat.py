import sys


if sys.version_info[0] < 3:
    def py3_compat(cls):
        return cls
else:
    def py3_compat(cls):
        cls.__str__ = cls.__unicode__
        del cls.__unicode__
