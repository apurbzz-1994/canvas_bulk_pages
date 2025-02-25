from canvasapi import Canvas

class BulkPageAdd:

    def __init__(self, canvas_url, canvas_key, title, content, subject_list):
        self.canvas_url = canvas_url
        self.canvas_key = canvas_key
        self.title = title
        self.content = content
        self.subject_list = subject_list
        self.canvas = Canvas(canvas_url, canvas_key)


    def add_page(self, subject_code):
        response = None

        try:
            subject = self.canvas.get_course(subject_code, use_sis_id=True, include=['concluded', 'term'])

            a_page = subject.create_page(wiki_page = {
                'title': self.title,
                'body': f"""{self.content}""",
                'published': False
            })
            full_page_url = {'status': 'success', 'm': f"Success - {self.canvas_url}courses/{subject.id}/pages/{a_page.url}"}
            response = full_page_url
        except Exception as e:
            error_message = {'status': 'error', 'm': f"Error, unable to add page - {e}"}
            response = error_message
        finally:
            return response


    def bulk_add_pages(self):
        all_subjects = self.subject_list.split(",")
        exec_messages = []

        for each_subject in all_subjects:
            message = self.add_page(each_subject)
            message['m'] = f"{each_subject}: {message['m']}"
            exec_messages.append(message)

        return exec_messages


        