from task import Task
from logger import log
from task_dao import TaskDAO

opcion = None

while opcion != 5:
    print('Opciones: ')
    print('1. Listar tareas')
    print('2. Agregar tarea')
    print('3. Modificar tarea')
    print('4. Eliminar tarea')
    print('5. Salir')
    opcion = int(input('Escribir opción (1-5)'))

    if opcion == 1:
        tareas = TaskDAO.select()
        for tarea in tareas:
            log.info(tarea)
    elif opcion == 2:
        titulo_var = input('Escribe el titulo: ')
        descripcion_var = input('Escribe la descripcion: ')
        tarea = Task(title=titulo_var, description=descripcion_var)
        tarea_insertada = TaskDAO.insert(tarea)
        log.info(f'Tarea insertada: {tarea_insertada}')

    elif opcion == 3:
        id_tarea_var = int(input('Escribe el id a modificar: '))
        titulo_var = input('Escribe el nuevo titulo: ')
        descripcion_var = input('Escribe la nueva descripción: ')
        tarea = Task(id_tarea_var, titulo_var, descripcion_var)
        tarea_actualizada = TaskDAO.update(tarea)
        log.info(f'Tarea actualizada: {tarea_actualizada}')

    elif opcion == 4:
        id_tarea_var = int(input('Escriba el id a eliminar: '))
        tarea = Task(id_task=id_tarea_var)
        tarea_eliminada = TaskDAO.delete(tarea)
        log.info(f'Tarea eliminada: {tarea_eliminada}')

    else:
        log.info('Salimos de la aplicación...')