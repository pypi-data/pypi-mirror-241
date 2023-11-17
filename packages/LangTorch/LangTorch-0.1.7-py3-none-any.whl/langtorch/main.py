import sys

sys.path.append("..")
import langtorch
from langtorch.tt import TextModule, Activation
from langtorch import TextTensor, ctx
from langtorch.tensors import ChatTensor, User, Assistant
from langtorch.tt import TextLoss
from langtorch import Session
from langtorch.texts import Text
from langtorch.api import auth
import numpy as np
import torch

session = Session("D://langtorch/session_1.yaml")
def modularize(func):

	def forward(tt):
		print(tt)
		assert isinstance(tt, TextTensor)
		result = np.array(func(tt.content.tolist()), dtype = object)
		if len(result) == tt.content.size:
			tt.content = result.reshape(tt.content.shape)
		elif (len(result) / tt.content.size) % 1 < 0.0001:
			tt.content = result.reshape(list(tt.shape) + [len(result) // tt.size])
		else:
			tt.content = result
		return tt

	result = torch.nn.Module()
	result.forward = forward
	return result

act = Activation()
# print(modularize(lambda xx: [f"_{x}_" for x in xx])(TextTensor([1,2,3,4,5,6,7,8,9]).reshape(3,3)))

print()

chain = torch.nn.Sequential(
	TextModule("Calculate this equation:\n"),
	langtorch.methods.CoT,
	Activation(),
	TextModule("Is this reasoning correct?\n"),
	Activation(T=0.)
)

p = Text(("greeting","Hello, world!")).add_key_("prompt")
pp = p+p
print(p)
pp.loc[['prompt']] = "test"
p.loc['prompt'] = "test"
# # Example usage:
# input = (User([f"Is {word} positive?" for word in ["love","chair","non-negative"]])*Assistant(["Yes", "No", "Yes"])).requires_grad_()  # Dummy tensors-like object with .content attribute
# target = TextTensor(['Yes',"No","No"]).requires_grad_()  # Dummy tensors-like object with .content attribute
# loss_fn = TextLoss(prompt = "")  # Create the loss function instance
# loss = loss_fn(input, target)  # Compute the loss
# loss.backward()  # Backpropagate the loss
