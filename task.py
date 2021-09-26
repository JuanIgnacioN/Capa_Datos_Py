class Task:
    def __init__(self, id_task=None, title=None, description=None):
        self._id_task = id_task
        self._title = title
        self._description = description

    def __str__(self):
        return f'''
        ID: {self._id_task}
        Title: {self._title}
        Description: {self._description}
        '''

    @property
    def id_task(self):
        return self._id_task

    @id_task.setter
    def id_task(self, id_task):
        self._id_task = id_task

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description