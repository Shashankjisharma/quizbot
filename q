#!/usr/bin/env python

# Copyright (C) 2012, 2013  Alexander Berntsen <alexander@plaimi.net>
# Copyright (C) 2012, 2013  Stian Ellingsen <stian@plaimi.net>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Simple quizbot that asks questions and awards points."""

import config
import sqlite3
import eliza
from time import sleep
from time import time

from getpass import getpass
from operator import itemgetter
from random import choice, shuffle
from sys import argv

from twisted.words.protocols import irc
from twisted.internet import protocol, reactor

import random
import os
import questions as q
import datetime
#import ascii as asciiart
#import shayari as shayaris

class Bot(irc.IRCClient):
    #answered_already={}
    quiz_on=0
    answered_question =0
    chat_bot =  eliza.eliza()
    now = datetime.datetime.now()
    logfile = open('logs','a',1)
    logfile.write("starting logs\n")
    print now
    logfile.write(str(now))
    """The bot procedures go here."""

    def _get_nickname(self):
        """Sets Bot nick to our chosen nick instead of defaultnick."""
        return self.factory.nickname
    nickname = property(_get_nickname)

    def connectionMade(self):
        """Overrides CONNECTIONMADE."""
        # Identifies with nick services if password is set.
        if config.password:
            self.password = self.factory.password
            self.username = self.factory.username
        self.quizzers = {}
        self.last_decide = 10
        self.answered = 5
        self.winner = ''
        self.question = ''
        #self.shayari = ''
        self.recently_asked = []
        self.db = sqlite3.connect(config.hiscoresdb)
        self.dbcur = self.db.cursor()
        self.dbcur.execute('CREATE TABLE IF NOT EXISTS hiscore (quizzer TEXT'
                           ' unique, wins INTEGER)')
        self.db.commit()
        self.hunger = 0
        self.complained = False
        irc.IRCClient.connectionMade(self)

    def signedOn(self):
        """Overrides SIGNEDON."""
        self.join(self.factory.channel)
        print "signed on as %s" % (self.nickname)

    def joined(self, channel):
        """Overrides JOINED."""
        print "joined %s" % channel
        #self.op(self.nickname)
        # Get all users in the chan.
        self.sendLine("NAMES %s" % self.factory.channel)
        reactor.callLater(5, self.reset)
        reactor.callLater(5, self.decide)
        #self.help("test")
        self.msg(self.factory.channel, 'Hello! I am %s. Type !help to know more about me' % (self.nickname))


    def userJoined(self, user, channel):
        """Overrides USERJOINED."""
        name = self.clean_nick(user)
        self.add_quizzer(name)
        self.complained = False
        self.msg(self.factory.channel, 'Hello %s, welcome!' % (name))
        self.logfile.write('\n%s joined' % (name))

    def userLeft(self, user, channel):
        """Overrides USERLEFT."""
        self.del_quizzer(user)
        self.logfile.write('\n%s left' % (user))

    def userQuit(self, user, channel):
        """Overrides USERQUIT."""
        self.del_quizzer(user)

    def userRenamed(self, oldname, newname):
        """Overrides USERRENAMED."""
        self.del_quizzer(oldname)
        self.add_quizzer(newname)

    def irc_RPL_NAMREPLY(self, prefix, params):
        """Overrides RPL_NAMEREPLY."""
        # Add all users in the channel to quizzers.
        for i in params[3].split():
            if i != self.nickname:
                self.add_quizzer(i)

    def privmsg(self, user, channel, msg):
        """Overrides PRIVMSG."""
        name = self.clean_nick(user)
        self.logfile.write('\n%s said %s' %(name,msg))
        self.logfile.write('\n')
        # Check for answers.
        #if not self.answered:
        #    if self.quizzers[name] is None:
        #        self.quizzers[name] = 0
        #    if str(self.answer).lower() in msg.lower():
        #        self.award(name)
        #    else:
        #        self.deduct(name)
        if channel == self.nickname:
          if user.startswith('nkshirsa'):
            self.msg(self.factory.channel, msg)
            return
          else:
            #self.msg(self.factory.channel, 'Type !help to see what I do %s' % (user))
            self.msg("nkshirsa", '%s is the message from %s' % (msg,user))
            return
            
        if msg.startswith(self.nickname):
            if self.quiz_on == 0: #general comment, not an answer since quiz is not on
              #self.msg(self.factory.channel, 'Type !help to see what I can do %s' % (user))
              query = str(msg)
              to_send = query.partition(" ")[2]
              reply = self.chat_bot.respond(to_send)
              userstr = str(user).partition("!")[0]
              self.msg(self.factory.channel, '%s, %s' % (userstr,reply))
              self.logfile.write('\n%s said %s and quizbot replied %s' %(userstr,to_send,reply))
              self.logfile.write("\n")
        else:
            word_list = msg.split()
            if self.nickname in msg:
                if self.quiz_on == 0: #general comment, not an answer since quiz is not on
                #self.msg(self.factory.channel, 'Type !help to see what I can do %s' % (user))
                  query = str(msg)
                  to_send1 = query.partition("quizbot")[0]
                  to_send2 = query.partition("quizbot")[2]
                  if len(to_send1) > len(to_send2):
                      to_send=to_send1
                  else:
                      to_send=to_send2
                      
                  reply = self.chat_bot.respond(to_send)
                  userstr = str(user).partition("!")[0]
                  self.msg(self.factory.channel, '%s, %s' % (userstr,reply))
                  self.logfile.write('\n%s said %s and quizbot replied %s' %(userstr,to_send,reply))
                  self.logfile.write('\n ')
                  #else:
 
        # Check if it's a command for the bot.
        if msg.startswith('!help'):
            try:
                # !help user
                self.help(msg.split()[1])
            except:
                # !help
                self.help(name)
        elif msg.startswith('!startquiz'):
            if self.quiz_on==1:
                userstr = str(user).partition("!")[0]
                self.msg(self.factory.channel, 'Cant start something thats already started, %s' % (userstr))
            else:
                self.msg(self.factory.channel, 'questions shall be posed starting now')
                self.quiz_on = 1
                self.logfile.write('\n %s started the quiz\n' %(user))
        elif msg.startswith('!shayari'):
            if(self.quiz_on==0):
               self.logfile.write('\n %s asked for shayari\n' %(user))
               self.shayari()
            else:
               userstr = str(user).partition("!")[0]
               self.msg(self.factory.channel, 'Sorry %s no Shayari during quiz!' % (userstr))
        elif msg.startswith('!stopquiz'):
            if self.quiz_on == 0:
                userstr = str(user).partition("!")[0]
                self.msg(self.factory.channel, 'Cant stop something thats already stopped, %s' % (userstr))
            else:
                self.msg(self.factory.channel, 'No further questions shall be posed')
                self.quiz_on = 0
                self.answered = 5
                self.logfile.write('\n %s stopped the quiz\n' %(user))
        elif msg.startswith('!reload'):
            self.reload_questions(name)
        elif msg.startswith('!botsnack'):
            self.feed()
        elif msg.startswith('!op'):
            self.op(name)
        elif msg.startswith('!deop'):
            self.deop(name)
        elif msg.startswith('!score'):
            self.print_score()
        elif msg.startswith('!hiscore'):
            self.print_hiscore()
        #all messages that start with the nickname of the bot are treated as answers 
        elif msg.startswith(self.nickname) and self.quiz_on == 1:
                    #print name
                    try:
                        if self.quizzers[name] is None:
                        #initialize points to 0 if no entry exists
                            self.quizzers[name] = 0
                    except Exception, e:
                            self.quizzers[name] = 0
                    self.logfile.write('\n%s answered %s' %(name,msg))
                    self.logfile.write('\n')
                    if str(self.answer).lower() in msg.lower():
                        if len(str(self.answer))>1:
                            if self.answered_question == 0:
                                self.award(name)
                            else:
                                self.msg(self.factory.channel, '%s, too late.. :-(' % (name))
                        elif len(str(self.answer))==1:
                            if self.answered_question==0:
                               word_list = msg.split()
                               #print word_list[-1] 
                               if len(str(word_list[-1]))>1:
                                   self.msg(self.factory.channel, '%s, Choose a number out of 1,2,3 or 4 please.. :-(' % (name))
                                   self.deduct(name)
                               elif len(str(word_list[-1]))==1:
                                   self.award(name)
                            else:
                                word_list = msg.split()
                                #print word_list[-1]
                                if len(str(word_list[-1]))==1:
                                    self.msg(self.factory.channel, '%s, too late.. :-(' % (name))
                    else:
                        if self.answered_question == 0:
                            self.deduct(name)

    def decide(self):
        """Figure out whether to post a question or a hint."""
        t = time()
        f, dt = ((self.ask, self.answered + 10 - t) if self.answered else
                 (self.hint, self.last_decide + 10 - t))
        if dt < 0.5:
           f()
           self.last_decide = t
           dt = 5
        reactor.callLater(min(10, dt), self.decide)

    def ask(self):
        self.answered_once = {} #reset to nobody answered
        """Ask a question."""
        #self.hunger += 1
        #if self.hunger > 6:
        #    if not self.complained:
        #        self.msg(self.factory.channel,
        #                 "I'm hungry. Please feed me with !botsnack.")
        #        #self.complained = True
        #    return
        # Make sure there have been ten questions in between this question.
        if self.quiz_on == 0:
            return
        self.msg(self.factory.channel, "****************************************************************************** ")
        self.answered_question = 0
        while self.question in self.recently_asked or not self.question:
            cqa = choice(q.questions)
            self.question = cqa[1]
        self.category = cqa[0]
        # This num should be changed depending on how many questions you have.
        if len(self.recently_asked) >= 10:
            self.recently_asked.pop(0)
        self.recently_asked.append(self.question)
        self.answer = cqa[2]
        self.msg(self.factory.channel, 'TOPIC: %s: %s' %
                (self.category, self.question))
        self.logfile.write('\n%s is question' %(self.question))
        if config.verbose:
            print '%s - %s - %s' % (self.category, self.question, self.answer)
        # Make list of hidden parts of the answer.
        self.answer_masks = range(len(str(self.answer)))
        # Set how many characters are revealed per hint.
        self.difficulty = max(len(str(self.answer)) / 6, 1)
        if isinstance(self.answer, str):
            # Shuffle them around to reveal random parts of it.
            shuffle(self.answer_masks)
        else:
            # Reveal numbers from left to right.
            self.answer_masks = self.answer_masks[::-1]
        # Number of hints given.
        self.hint_num = 0
        # Time of answer.  0 means no answer yet.
        self.answered = 0
        #self.msg(self.factory.channel, 'questions shall be posed starting now')
 
    def ascii_art(self):
        asciiname = open("outputascii",'r')
        ascii_name = asciiname.readlines()
        for a_line in ascii_name:
            self.msg(self.factory.channel, '%s' % (a_line))
        asciiname.close()
        f = open("ascii.py",'r')
        pic = f.readlines()
        for line in pic:
          self.msg(self.factory.channel, '%s' % (line))
        f.close()

    def shayari(self):
        #data = [line.strip() for line in open("shayari.py",'r')]
        #shay = open("shayari.py").read()
        shay = open("shayari.py")
        shayaris = shay.readlines()
        count = shayaris[0]
        count_int = int(count)
        # random number between 1 and count
        whichone = random.randint(1,count_int)
        shayari = shayaris[whichone].decode("utf-8")
        self.msg(self.factory.channel, '%s' % (shayari))

    def hint(self):
        print self.hint_num
        """Give a hint."""
        # Max 5 hints, and don't give hints when the answer is so short.
        if self.quiz_on == 0:
            return
        if len(str(self.answer)) <= self.hint_num + 1 or self.hint_num >= 5:
            #if (len(str(self.answer)) == 1 and self.hint_num == 0):
            if self.hint_num >=5:
                self.fail()
            elif len(str(self.answer)) == 1:
                self.msg(self.factory.channel, 'HINT: Please input a number!')
            self.hint_num += 1
            return
        # Reveal difficulty amount of characters in the answer.
        for i in range(self.difficulty):
            try:
                # If hint is ' ', pop again.
                while self.answer_masks.pop() == ' ':
                    pass
            except:
                pass
        self.answer_hint = ''.join(
            '*' if idx in self.answer_masks and c is not ' ' else c for
            idx, c in enumerate(str(self.answer)))
        self.msg(self.factory.channel, 'HINT: %s' % self.answer_hint)
        self.logfile.write('\n%s is hint\n'%(self.answer_hint))
        self.hint_num += 1

    def fail(self):
        """Timeout/giveup on answer."""
        self.msg(self.factory.channel, 'Time is UP ! onto the next question!')
        #self.msg(self.factory.channel, 'the answer was: "%s"' % self.answer)
        self.answered = time()

    def deduct(self, awardee):
        """deducts a point from awardee."""
        if self.quizzers[awardee] == 0:
            self.msg(self.factory.channel, 'wrong! But %s already at 0, showing mercy!' %
                (awardee)) 
        else:
            self.quizzers[awardee] -= 1
            self.msg(self.factory.channel, 'wrong! deducting one point for %s!' %
                (awardee))
        self.logfile.write('\n%s incorrectly answered ' %(awardee))
        self.logfile.write('\n')

    def award(self, awardee):
        """Gives a point to awardee."""
        self.quizzers[awardee] += 1
        self.msg(self.factory.channel, '%s is right! congratulations, %s!' %
                (self.answer, awardee))
        self.logfile.write('\n%s correctly answered %s' %(awardee,self.answer))
        self.logfile.write('\n')
        self.answered = 1
        self.answered_question = 1
        if self.quizzers[awardee] >= self.target_score:
            self.win(awardee)
            self.logfile.write('\n%s wins the quiz' %(awardee))
        #self.hunger = max(0, self.hunger - 1)
        self.print_score()
        self.answered = time()

    def win(self, winner):
        """Is called when target score is reached."""
        numAnswerers = 0
        quizzersByPoints = sorted(self.quizzers.iteritems(), key=itemgetter(1),
                                  reverse=True)
        for numAnswerers, (quizzer, points) in enumerate(quizzersByPoints):
            if points is None:
                break
        else:
            numAnswerers += 1
        if numAnswerers > 1:
            winner = quizzersByPoints[0][0]
            self.dbcur.execute('SELECT * FROM hiscore WHERE quizzer=?',
                               (winner,))
            wins = 1
            row = self.dbcur.fetchone()
            if row is not None:
                wins = row[1] + 1
                sql = 'UPDATE hiscore SET wins = ? WHERE quizzer = ?'
            else:
                sql = 'INSERT INTO hiscore (wins,quizzer) VALUES (?,?)'
            self.dbcur.execute(sql, (wins, winner))
            self.db.commit()

        self.winner = winner
        self.msg(self.factory.channel, 'congratulations to %s, the winner!!!' % self.winner)
        self.msg(self.factory.channel, "****************************************************************************** ")
        self.msg(self.factory.channel, "****************************************************************************** ")
        #art = cprint(figlet_format('missile!', font='starwars'), 'yellow', 'on_red', attrs=['bold'])
        os.system('rm outputascii')
        os.system('python test.py %s > outputascii' % (self.winner))
        self.ascii_art();
        #self.msg(self.factory.channel, "New Quiz starting !")
        self.msg(self.factory.channel, "****************************************************************************** ")
        self.reset()
        self.quiz_on=0
        self.help(winner)

    def help(self, user):
        """Message help message to the user."""
        # Prevent spamming to non-quizzers, AKA random Freenode users.
        #if user not in self.quizzers and user is not "test":
        #   print "returning from help"
        #  return
        self.msg(self.factory.channel, "****************************************************************************** ")
        self.msg(self.factory.channel, "****************************************************************************** ")
        self.msg(self.factory.channel, 'I am ' + self.nickname + ', and I ask questions.')
        self.msg(self.factory.channel, 'Plus 1 for right answers, minus 1 for wrong answers. Reach 10 points to win!')
        self.msg(self.factory.channel, '!startquiz and !stopquiz starts and stops the quiz.')
        self.msg(self.factory.channel, 'During the quiz, answer this way: %s, YOUR ANSWER' % (self.nickname))
        self.msg(self.factory.channel, "****************************************************************************** ")
        self.msg(self.factory.channel, 'Please provide feedback on https://docs.google.com/document/d/11DSlUQPc69DjA4cMNA1vaEo4AvdYW2VV0IAoM5IHRpk')
        self.msg(self.factory.channel, 'If not quizzing, feel free to talk to me I have some interesting opinions!')
        self.msg(self.factory.channel, 'Oh, and for shayari, type !shayari')

    def reload_questions(self, user):
        """Reload the question/answer list."""
        if self.is_p(user, self.factory.masters):
            reload(q)
            self.msg(self.factory.channel, 'reloaded questions.')

    def feed(self):
        """Feed quizbot."""
        self.hunger = 0
        self.complained = False
        self.msg(self.factory.channel, 'ta. :-)')

    def op(self, user):
        """OP a master."""
        if self.is_p(user, self.factory.masters):
            self.msg('CHANSERV', 'op %s %s' % (self.factory.channel, user))

    def deop(self, user):
        """DEOP a master."""
        if self.is_p(user, self.factory.masters):
            self.msg('CHANSERV', 'deop %s %s' % (self.factory.channel, user))

    def print_score(self):
        """Print the top five quizzers."""
        prev_points = -1
        for i, (quizzer, points) in enumerate(
                sorted(self.quizzers.iteritems(), key=itemgetter(1),
                       reverse=True)[:5], 1):
            if points:
                if points != prev_points:
                    j = i
                self.msg(self.factory.channel, '%d. %s: %d points' %
                         (j, quizzer, points))
                prev_points = points

    def print_hiscore(self):
        """Print the top five quizzers of all time."""
        self.dbcur.execute('SELECT * FROM hiscore ORDER by wins DESC LIMIT 5')
        hiscore = self.dbcur.fetchall()
        for i, (quizzer, wins) in enumerate(hiscore):
            self.msg(self.factory.channel, '%d. %s: %d points' %
                    (i + 1, quizzer.encode('UTF-8'), wins))

    def set_topic(self):
        self.dbcur.execute('SELECT * FROM hiscore ORDER by wins DESC LIMIT 1')
        alltime = self.dbcur.fetchone()
        if alltime is None:
            alltime = ["no one", 0]
        self.topic(
            self.factory.channel,
            'happy quizzing. :-> target score: %d. previous winner: %s. '
            'all-time winner: %s (%d).' %
            (self.target_score, self.winner, alltime[0].encode('UTF-8'),
             alltime[1]))

    def reset(self):
        """Set all quizzers' points to 0 and change topic."""
        for i in self.quizzers:
            self.quizzers[i] = None
        #self.target_score = 1 + len(self.quizzers) / 2
        self.target_score = 10
        #self.set_topic()

    def add_quizzer(self, quizzer):
        """Add quizzer from quizzers."""
        if quizzer == self.nickname or quizzer == '@' + self.nickname:
            return
        if quizzer not in self.quizzers:
            self.quizzers[quizzer] = 0

    def del_quizzer(self, quizzer):
        """Remove quizzer from quizzers."""
        if quizzer == self.nickname or quizzer == '@' + self.nickname:
            return
        if quizzer in self.quizzers:
            del self.quizzers[quizzer]

    def is_p(self, name, role):
        """Check if name is role."""
        try:
            if name in role:
                return True
        except:
            if name == role:
                return True
        if role == self.quizzers:
            return False
        self.msg(self.factory.channel, 'not on my watch, %s!' % name)
        #self.kick(self.factory.channel, name, 'lol.')
        #self.del_quizzer(name)
        return False

    def clean_nick(self, nick):
        """Cleans the nick if we get the entire name from IRC."""
        nick = nick.split('!')[0]
        if nick[0] == '~':
            nick = nick.split('~')[1]
        return nick


class BotFactory(protocol.ClientFactory):

    """The bot factory."""

    protocol = Bot

    def __init__(self, channel):
        self.channel = channel
        self.nickname = config.nickname
        self.username = config.username
        if config.password:
            self.password = getpass('enter password (will not be echoed): ')
        self.masters = config.masters

    def clientConnectionLost(self, connector, reason):
        print "connection lost: (%s)\nreconnecting..." % reason
        connector.connect()

    def clientConnectionFailed(self, connector, reason):
        print "couldn't connect: %s" % reason

if __name__ == "__main__":
    if len(argv) > 1:
        print """
        edit config.py.

        start program with:
        $ ./q

        if you have set password in config, it will ask for it.
        """
    else:
        reactor.connectTCP(config.network, config.port,
                           BotFactory('#' + config.chan))
        reactor.run()