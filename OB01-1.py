# Задача: Создай класс `Task`, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено).
# Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка текущих (не выполненных) задач.

class Task():
    def __init__(self):
        self.tasks = []

    def add_task(self, discr, deadline):
        task = {"discr": discr, "deadline": deadline, "status": False}
        self.tasks.append(task)
    def mark_task_compl(self, discr):
        for task in self.tasks:
            if task["discr"] == discr:
                task["status"] = True
                break

    def info_tasks(self):
        print("Текущие задачи:")
        for task in self.tasks:
            if not task["status"]:
                print(f'Задача: {task["discr"]}, Срок: {task["deadline"]}, Статус: {"не выполнено"}')


Home_task = Task()
Home_task.add_task("Сделать ДЗ по питону OB01","31.03.2024")
Home_task.add_task("Сделать ДЗ по питону OB02","31.03.2024")
Home_task.info_tasks()
Home_task.mark_task_compl("Сделать ДЗ по питону OB01")
Home_task.info_tasks()