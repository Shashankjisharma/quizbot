import eliza
import sys
therapist = eliza.eliza()
reply = therapist.respond(sys.argv[1])
print reply

