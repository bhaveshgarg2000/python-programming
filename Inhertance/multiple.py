class A:
    def feature_1(self):
        print("Feature 1 Working")

    def feature_2(self):
        print("Feature 2 Working")


class B:
    def feature_3(self):
        print("Feature 3 Working")
    def feature_4(self):
        print("Feature 4 Working")



class C(A,B):
    def feature_5(self):
        print("Feature 5 Working")
    def feature_6(self):
        print("Feature 6 Working")


c1 = C()
print("MULTI LEVEL INHERITANCE")
c1.feature_1()