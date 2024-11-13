# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Solution 1 
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0

        # l1과 l2의 모든 노드를 순회
        while l1 or l2:
            # l1, l2 노드 값이 있다면 가져오고 없으면 0으로 설정
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            
            # 두 값과 carry를 더한 후, 10으로 나눈 나머지와 몫을 계산
            total = x + y + carry
            carry = total // 10
            new_val = total % 10

            # 새로운 노드를 결과 리스트에 추가
            current.next = ListNode(new_val)
            current = current.next

            # l1과 l2가 각각 다음 노드로 이동
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        # 모든 노드 순회 후 carry가 남아 있다면 마지막 노드에 추가
        if carry > 0:
            current.next = ListNode(carry)

        # dummy_head 다음 노드를 반환하여 결과 리스트 반환
        return dummy_head.next
    
# Solution 2 : time, memory better
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0

        # 반복문을 통해 l1과 l2 노드를 동시에 순회
        while l1 or l2 or carry:
            # 각 노드의 값을 더하고 자리 올림을 계산
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next

            # carry의 일의 자리를 새 노드의 값으로 추가하고 자리 올림 갱신
            current.next = ListNode(carry % 10)
            current = current.next
            carry //= 10  # 자리 올림만 남김

        # 결과 연결 리스트의 시작점 반환
        return dummy_head.next