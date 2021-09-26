from cursor import Cursor
from task import Task
from logger import log


class TaskDAO:
    _SELECT = 'SELECT * FROM task ORDER BY id_task'
    _INSERT = 'INSERT INTO task (title, description) VALUES (%s, %s)'
    _UPDATE = 'UPDATE task SET title=%s, description=%s WHERE id_task=%s'
    _DELETE = 'DELETE FROM task WHERE id_task=%s'

    @classmethod
    def select(cls):
        with Cursor() as cursor:
            cursor.execute(cls._SELECT)
            registros = cursor.fetchall()
            tasks = []
            for registro in registros:
                task = Task(registro[0], registro[1], registro[2])
                tasks.append(task)
        return tasks

    @classmethod
    def insert(cls, task):
        with Cursor() as cursor:
            log.debug(f'Tarea a insertar: {task}')
            valores = (task.title, task.description)
            cursor.execute(cls._INSERT, valores)
            log.debug(f'Tarea insertado correctamente: {task}')
            return cursor.rowcount

    @classmethod
    def update(cls, task):
        with Cursor() as cursor:
            log.debug(f'Tarea a actualizar: {task}')
            valores = (task.title, task.description, task.id_task)
            cursor.execute(cls._UPDATE, valores)
            return cursor.rowcount

    @classmethod
    def delete(cls, task):
        with Cursor() as cursor:
            valores = (task.id_task,)
            cursor.execute(cls._DELETE, valores)
            log.debug(f'Tarea eliminada: {task}')
            return cursor.rowcount
