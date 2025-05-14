class Head:
    def __init__(self, eyes, mouth, ears):
        self.eyes = eyes
        self.mouth = mouth
        self.ears = ears

class Hand:
    def __init__(self,hand_fingers):
        self.hand_fingers = hand_fingers

class Arm:
    def __init__(self, hand):
        self.hand = hand

class Feet:
    def __init__(self, feet_fingers):
        self.feet_fingers = feet_fingers

class Leg:
    def __init__(self, feet):
        self.feet = feet

class Torso:
    def __init__(self, head, left_arm, right_arm, left_leg, right_leg):
        self.head = head
        self.left_arm = left_arm
        self.right_arm = right_arm
        self.left_leg = left_leg
        self.right_leg = right_leg

class Human:
    def __init__(self):
        eyes = 2
        ears = 2
        mouth = 1
        head = Head(eyes,mouth,ears)
        left_hand_fingers = 5
        right_hand_fingers = 5
        left_hand = Hand(left_hand_fingers)
        right_hand = Hand(right_hand_fingers)
        left_arm = Arm(left_hand)
        right_arm = Arm(right_hand)
        left_feet_fingers = 5
        right_feet_fingers = 5
        left_foot = Feet(left_feet_fingers)
        right_foot = Feet(right_feet_fingers)
        left_leg = Leg(left_foot)
        right_leg = Leg(right_foot)

        self.torso = Torso(head, left_arm, right_arm, left_leg, right_leg)

human = Human()
print(human.torso.head.eyes, human.torso.head.ears)
print(human.torso.left_arm.hand.hand_fingers)
print(human.torso.right_leg.feet.feet_fingers)