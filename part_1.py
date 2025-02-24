class ListNode:
    """
    Клас для вузла однозв'язного списку.
    """

    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


class LinkedList:
    """
    Клас для однозв'язного списку з базовими методами.
    """

    def __init__(self):
        self.head = None

    def append(self, value):
        """
        Додає новий вузол у кінець списку.
        """
        if not self.head:
            self.head = ListNode(value)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = ListNode(value)

    def print_list(self):
        """
        Виводить всі елементи списку.
        """
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

    def reverse(self):
        """
        Реверсує однозв'язний список, змінюючи посилання між вузлами.
        """
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def merge_sorted_lists(self, l1, l2):
        """
        Об'єднує два відсортовані однозв'язні списки в один відсортований список.
        """
        dummy = ListNode()  # Фіктивний вузол
        tail = dummy
        while l1 and l2:
            if l1.value < l2.value:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        tail.next = l1 if l1 else l2
        self.head = dummy.next

    def sort(self):
        """
        Сортує однозв'язний список методом злиття (Merge Sort).
        """
        if not self.head or not self.head.next:
            return self.head

        def get_middle(node):
            slow, fast = node, node.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        def merge_sort(node):
            if not node or not node.next:
                return node
            middle = get_middle(node)
            next_to_middle = middle.next
            middle.next = None
            left = merge_sort(node)
            right = merge_sort(next_to_middle)
            return merge(left, right)

        def merge(l1, l2):
            dummy = ListNode()
            tail = dummy
            while l1 and l2:
                if l1.value < l2.value:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next
            tail.next = l1 if l1 else l2
            return dummy.next

        self.head = merge_sort(self.head)


# Приклад використання
ll = LinkedList()
for value in [4, 2, 1, 3]:
    ll.append(value)
print("Оригінальний список:")
ll.print_list()

print("Реверсований список:")
ll.reverse()
ll.print_list()

print("Відсортований список:")
ll.sort()
ll.print_list()
