class runnr_flags:
    s_file_name : str
    s_extension : str
    s_custom_output_file_name : str
    s_extra_param : str
    s_extra_args : str
    s_lib_link : str
    l_file_names : list

    b_run_after_compilatiion : bool
    b_debug_mode : bool
    b_link_add_l : bool

    def __init__(self):
        self.b_run_after_compilatiion = True
        self.b_debug_mode = False
        self.b_multiple_files = False

        self.l_file_names = []

        self.s_file_name = ''
        self.s_extension = ''
        self.s_extra_param = ''
        self.s_extra_args = ''
        self.s_custom_output_file_name = ''
        self.s_lib_link = ''
        self.b_link_add_l = True
