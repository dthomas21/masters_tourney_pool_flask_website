from flask_table import Table, Col, LinkCol


class Results(Table):
    id = Col('Id', show=False)
    entry_email = Col('Entrant Email')
    entrant_full_name = Col('Entrant Full Name')
    team_name = Col('Team Name')
    golfer_1 = Col('Golfer 1')
    golfer_2 = Col('Golfer 2')
    golfer_3 = Col('Golfer 3')
    golfer_4 = Col('Golfer 4')
    tie_breaker = Col('Tie Breaker')
    has_paid = Col('Paid?')
#     For editing and deleting data:
    edit = LinkCol('Edit', 'edit', url_kwargs=dict(id='id'))
    delete = LinkCol('Delete', 'delete', url_kwargs=dict(id='id'))

class UserResults(Table):
    id = Col('Id', show=False)
    # entry_email = Col('Entrant Email')
    entrant_full_name = Col('Entrant Full Name')
    team_name = Col('Team Name')
    golfer_1 = Col('Golfer 1')
    golfer_2 = Col('Golfer 2')
    golfer_3 = Col('Golfer 3')
    golfer_4 = Col('Golfer 4')
    tie_breaker = Col('Tie Breaker')
    has_paid = Col('Paid?')
#     For editing and deleting data:
#     edit = LinkCol('Edit', 'edit', url_kwargs=dict(id='id'))
#     delete = LinkCol('Delete', 'delete', url_kwargs=dict(id='id'))
