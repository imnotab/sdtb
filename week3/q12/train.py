import torch
from torch import nn

torch.manual_seed(20260907)
x = torch.linspace(-1, 1, 101).reshape(-1, 1)
y = 3 * x - 1

loss_fn = nn.MSELoss()
model = nn.Linear(1, 1)
opt = torch.optim.SGD(model.parameters(), lr=0.1)

for _ in range(200):
    pred = model(x)
    loss = loss_fn(pred, y)
    # 清空梯度、反向传播、更新参数
    opt.zero_grad()
    loss.backward()
    opt.step()

# 训练完成，评估模式 + no_grad 计算最终损失
model.eval()
with torch.no_grad():
    final_pred = model(x)
    final_loss = loss_fn(final_pred, y)
    w = model.weight.item()
    b = model.bias.item()

print(f"final loss: {final_loss:.6f}")
print(f"weight: {w:.4f}")
print(f"bias: {b:.4f}")
