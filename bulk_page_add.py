from canvasapi import Canvas

class BulkPageAdd:

    def __init__(self, canvas_url, canvas_key, content, subject_list):
        self.canvas_url = canvas_url
        self.canvas_key = canvas_key
        self.content = content
        self.subject_list = subject_list
        self.canvas = Canvas(canvas_url, canvas_key)


    def add_page(self, subject_code):
        subject = self.canvas.get_course(subject_code, use_sis_id=True, include=['concluded', 'term'])

        subject.create_page(wiki_page = {
            'title': 'Test 2',
            'body': f"""{self.content}""",
            'published': False
        })
        print("Page added!")

    def bulk_add_pages(self):
        all_subjects = self.subject_list.split(",")
        success_code = 0

        for each_subject in all_subjects:
            self.add_page(each_subject)

        success_code = 1

        return success_code


        