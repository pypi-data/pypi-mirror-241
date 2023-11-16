def pre_update(self):  # type: ignore[no-untyped-def]
    import base64

    if self.data is not None:
        data = self.data
        bytes_data = base64.b64decode(data.encode() if isinstance(data, str) else data)
        self.size = len(bytes_data)
