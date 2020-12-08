
tracker_label = 'LEAST';

tracker_command = generate_python_command('vot_wrapper', ...
    {'/home/wcz/Yang/LEAST/pytracking/', ...
    '/media/wcz/datasets/yang/vot-toolkit/native/trax/support/python/',...
   '/home/wcz/Yang/LEAST/' });

tracker_interpreter = 'python';

tracker_linkpath = {'/media/wcz/datasets/yang/vot-toolkit/native/trax/build/'};
