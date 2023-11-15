import contextvars
from contextlib import contextmanager


class Missing(object):
    def __repr__(self):
        return "no value"

    def __bool__(self):
        return False


_missing = Missing()


class Setting(object):
    _tls = contextvars.ContextVar("_tls")

    @contextmanager
    def __call__(self, **options):
        """
        options:
            raw_response: 为True则返回原始httpx.Response对象, 为False返回解析好的业务Content对象
        """
        token = self._tls.set(options)
        yield
        self._tls.reset(token)

    def __getattribute__(self, key):
        if key != "_tls":
            try:
                options = self._tls.get()
            except LookupError:
                return _missing
            return options[key] if key in options else _missing
        return super().__getattribute__(key)
