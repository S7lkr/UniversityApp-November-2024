class PlaceholderMixin:
    def attach_placeholders(self):
        for field_name, field in self.fields.items():
            placeholder = field.label or field_name.replace('_', ' ').capitalize()
            field.widget.attrs['placeholder'] = placeholder + "..."

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.attach_placeholders()


class ReadOnlyFieldsMixin:
    readonly_fields_set = []

    def readonly_fields(self):
        for field_name in self.readonly_fields:     # iterate through the above array
            if field_name in self.fields:           # check if there really is such a field in the form
                self.fields[field_name].widget.attrs['readonly'] = True     # attach an attribute "readonly"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.readonly_fields()


class DisabledFieldsMixin:
    def disable_fields(self):
        for field_name, field in self.fields:
            if field_name in self.fields:
                self.fields[field_name].widget.attrs['disabled'] = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.disable_fields()
