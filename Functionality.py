from database import *


def ticket_trigger():
    c.execute('create trigger ticket_discount '
              'before INSERT on TICKET '
              'for each row if Ticket.age < 18 set Ticket.price - 60')
