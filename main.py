from models.LightBulb.LightBulb import LightBulb
from models.StateRepresentation.StateRepresentation import RepresentState


BedroomLight = LightBulb("Bedroom Light")
print("Light state is ", BedroomLight.state)

BedroomLight.turn_on()
print("Light state is ", BedroomLight.state)

BedroomLight.turn_off()
print("Light state is ", BedroomLight.state)


RepresentState.print(BedroomLight)
