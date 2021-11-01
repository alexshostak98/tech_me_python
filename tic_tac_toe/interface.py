from templates import interface_string, input_template_variants, template_variants


def user_interface(template_name: str, **template_vars):
    if template_name in input_template_variants:
        ask_str = input_template_variants[template_name](interface_string[template_name], **template_vars)
        user_input = input(ask_str)
        return user_input
    elif template_name in template_variants:
        print(template_variants[template_name](interface_string[template_name], **template_vars))
    else:
        print(interface_string[template_name])