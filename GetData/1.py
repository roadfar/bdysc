for j, field_name in enumerate(lookup_opts.admin.list_display):
    row_class = ''
    try:
        f = lookup_opts.get_field(field_name)
    except meta.FieldDoesNotExist:
        # For non-field list_display values, the value is a method
        # name. Execute the method.
        try:
            result_repr = strip_tags(str(getattr(result, field_name)()))
        except ObjectDoesNotExist:
            result_repr = EMPTY_CHANGELIST_VALUE