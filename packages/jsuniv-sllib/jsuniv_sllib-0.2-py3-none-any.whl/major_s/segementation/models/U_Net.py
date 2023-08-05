from collections import OrderedDict
import torch
import torch.nn as nn


class UNet(nn.Module):

    def __init__(self, in_channels=3, num_classes=1, init_features=32):
        super(UNet, self).__init__()

        features = init_features
        self.encoder1 = UNet._block(in_channels, features, name="enc1")
        self.pool1 = nn.MaxPool2d(kernel_size=2, stride=2)
        self.encoder2 = UNet._block(features, features * 2, name="enc2")
        self.pool2 = nn.MaxPool2d(kernel_size=2, stride=2)
        self.encoder3 = UNet._block(features * 2, features * 4, name="enc3")
        self.pool3 = nn.MaxPool2d(kernel_size=2, stride=2)
        self.encoder4 = UNet._block(features * 4, features * 8, name="enc4")
        self.pool4 = nn.MaxPool2d(kernel_size=2, stride=2)

        self.bottleneck = UNet._block(features * 8, features * 16, name="bottleneck")

        self.upconv4 = nn.ConvTranspose2d(
            features * 16, features * 8, kernel_size=2, stride=2
        )
        self.decoder4 = UNet._block((features * 8) * 2, features * 8, name="dec4")
        self.upconv3 = nn.ConvTranspose2d(
            features * 8, features * 4, kernel_size=2, stride=2
        )
        self.decoder3 = UNet._block((features * 4) * 2, features * 4, name="dec3")
        self.upconv2 = nn.ConvTranspose2d(
            features * 4, features * 2, kernel_size=2, stride=2
        )
        self.decoder2 = UNet._block((features * 2) * 2, features * 2, name="dec2")
        self.upconv1 = nn.ConvTranspose2d(
            features * 2, features, kernel_size=2, stride=2
        )
        self.decoder1 = UNet._block(features * 2, features, name="dec1")

        self.conv = nn.Conv2d(
            in_channels=features, out_channels=num_classes, kernel_size=1
        )

    def forward(self, x):
        # 编码器
        enc1 = self.encoder1(x);print('enc1:', enc1.size())
        enc2 = self.encoder2(self.pool1(enc1));print('enc2:', enc2.size())
        enc3 = self.encoder3(self.pool2(enc2));print('enc3:', enc3.size())
        enc4 = self.encoder4(self.pool3(enc3));print('enc4:', enc4.size())

       # bottleneck
        bottleneck = self.bottleneck(self.pool4(enc4));print('bottleneck:', bottleneck.size())

       # 解码器
        dec4 = self.upconv4(bottleneck);print('dec4:', dec4.size())
        dec4 = torch.cat((dec4, enc4), dim=1);print('dec4:', dec4.size())  # 那根线
        dec4 = self.decoder4(dec4);print('dec4:', dec4.size())

        dec3 = self.upconv3(dec4);print('dec3:', dec3.size())
        dec3 = torch.cat((dec3, enc3), dim=1);print('dec3:', dec3.size())
        dec3 = self.decoder3(dec3);print('dec3:', dec3.size())

        dec2 = self.upconv2(dec3);print('dec2:', dec2.size())
        dec2 = torch.cat((dec2, enc2), dim=1);print('dec2:', dec2.size())
        dec2 = self.decoder2(dec2);print('dec2:', dec2.size())

        dec1 = self.upconv1(dec2);print('dec1:', dec1.size())
        dec1 = torch.cat((dec1, enc1), dim=1);print('dec1:', dec1.size())
        dec1 = self.decoder1(dec1);print('dec1:', dec1.size())

        return torch.sigmoid(self.conv(dec1))

    @staticmethod
    def _block(in_channels, features, name):
        return nn.Sequential(
            OrderedDict(
                [
                    (
                        name + "conv1",
                        nn.Conv2d(
                            in_channels=in_channels, # 确定卷积核的深度
                            out_channels=features, # 确实输出的特征图深度，即卷积核组的多少
                            kernel_size=3,
                            padding=1,
                            bias=False,
                        ),
                    ),
                    (name + "norm1", nn.BatchNorm2d(num_features=features)),
                    (name + "relu1", nn.ReLU(inplace=True)),
                    (
                        name + "conv2",
                        nn.Conv2d(
                            in_channels=features,
                            out_channels=features,
                            kernel_size=3,
                            padding=1,
                            bias=False,
                        ),
                    ),
                    (name + "norm2", nn.BatchNorm2d(num_features=features)),
                    (name + "relu2", nn.ReLU(inplace=True)),
                ]
            )
        )

if __name__ == "__main__":
    # 随机生成输入数据
    rgb = torch.randn(1, 3, 360, 480)
    # 定义网络
    net = UNet(in_channels=3,num_classes=8)
    # 前向传播
    out = net(rgb)
    # 打印输出大小
    print('-----'*5)
    print(out.shape)
    print('-----'*5)

