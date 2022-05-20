import jinja2
import yaml

examples_to_render = [
    {   'context_yaml_path': 'archived_shortlist.yaml',
        'template_j2_path': 'archived.j2',
        'email_subject': '/lustre data archived',
        'rendered_filename':'archived_shortlist_email.txt'},
    
    {   'context_yaml_path': 'deleted_shortlist.yaml',
        'template_j2_path': 'deleted.j2',
        'email_subject': '/lustre data deleted',
        'rendered_filename':'deleted_shortlist_email.txt'},

    {   'context_yaml_path': 'warned_shortlist.yaml',
        'template_j2_path': 'warned.j2',
        'email_subject': '/lustre data deletion: 10 days notice',
        'rendered_filename':'warned_shortlist_email.txt'},

    {   'context_yaml_path': 'archived_longlist.yaml',
        'template_j2_path': 'archived.j2',
        'email_subject': '/lustre data archived',
        'rendered_filename':'archived_longlist_email.txt'},

    {   'context_yaml_path': 'deleted_longlist.yaml',
        'template_j2_path': 'deleted.j2',
        'email_subject': '/lustre data deleted',
        'rendered_filename':'deleted_longlist_email.txt'},

    {   'context_yaml_path': 'warned_longlist.yaml',
        'template_j2_path': 'warned.j2',
        'email_subject': '/lustre data deletion: 10 days notice',
        'rendered_filename':'warned_longlist_email.txt'}
] 

for example in examples_to_render:
    templateLoader = jinja2.FileSystemLoader(searchpath="./")
    templateEnv = jinja2.Environment(loader=templateLoader)
    template = templateEnv.get_template(example['template_j2_path'])

    with open('example_contexts/' + example['context_yaml_path'], 'r') as stream:
        try:
            context_yaml=yaml.safe_load(stream)
            #print(context_yaml)
        except yaml.YAMLError as exc:
            print(exc)

    with open('rendered/' + example['rendered_filename'], "w") as file_:
        file_.write('--- example templated email ---\n')
        file_.write('--- email subject: ' + example['email_subject'] + ' ---\n')
        file_.write('--- start email ---\n')
        file_.write(template.render(context_yaml))
        file_.write('\n--- end email ---\n')

        print('--- example templated email ---')
        print('--- email subject: ' + example['email_subject'] + ' ---')
        print('--- start email ---')
        print(template.render(context_yaml))
        print('--- end email ---')
