from tree import TreeNode
from tree import Tree

def resolve_fight(employee_report_structure):
    company_tree = Tree()
    print employee_report_structure
    relationship_list = employee_report_structure.split(',')
    fighting_employees = []
    fighting_employees.extend(relationship_list[-1:])
    del relationship_list[-1:]
    fighting_employees.extend(relationship_list[-1:])
    del relationship_list[-1:]
    print relationship_list
    print fighting_employees
    for str1 in employee_report_structure:
        temp = str1.split('->')
        mngr_name = temp[1]
        emp_name = temp[0]
        company_tree.add_employee(TreeNode(emp_name,mngr_name))



resolve_fight("Frank->Mary,Mary->Sam,Mary->Bob,Sam->Katie,Sam->Pete,Bob->John,Bob,Katie")