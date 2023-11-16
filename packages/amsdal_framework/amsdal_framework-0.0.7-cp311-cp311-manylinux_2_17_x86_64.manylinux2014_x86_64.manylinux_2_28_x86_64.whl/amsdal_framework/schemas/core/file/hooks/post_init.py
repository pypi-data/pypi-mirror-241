from typing import Any


def post_init(self, is_new_object: bool, kwargs: dict[str, Any]):  # type: ignore[no-untyped-def] # noqa: ARG001 FBT001
    import ast

    from amsdal_models.utils.files import convert_data_to_base64

    try:
        if isinstance(self.data, bytes):
            decoded_data = self.data.decode()
            if decoded_data.startswith("b'"):
                new_value = ast.literal_eval(decoded_data)
                if isinstance(new_value, bytes):
                    self.data = new_value
    except Exception:
        ...

    if self.data is not None:
        self.data = convert_data_to_base64(self.data)
