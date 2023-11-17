import torch
import torch.nn as nn
import torch.nn.functional as F

class ImagePyramid(nn.Module):
    def __init__(self, device="cpu") -> None:
        super(ImagePyramid, self).__init__()
        self.device = torch.device(device)
        self.kernel_dim3 = self._gauss_kernel(channels=3)
        self.kernel_dim1 = self._gauss_kernel(channels=1)
    
    def _gauss_kernel(self, channels=3):
        kernel = torch.tensor([[1., 4., 6., 4., 1],
                               [4., 16., 24., 16., 4.],
                               [6., 24., 36., 24., 6.],
                               [4., 16., 24., 16., 4.],
                               [1., 4., 6., 4., 1.]])
        kernel /= 256.
        kernel = kernel.repeat(channels, 1, 1, 1).to(self.device)
        return kernel
    
    def _downsample(self, x):
        return x[:, :, ::2, ::2]
    
    def _upsample(self, x):
        cc = torch.cat([x, torch.zeros(x.shape[0], x.shape[1], x.shape[2], x.shape[3], device=x.device)], dim=3)
        cc = cc.view(x.shape[0], x.shape[1], x.shape[2]*2, x.shape[3])
        cc = cc.permute(0,1,3,2)
        cc = torch.cat([cc, torch.zeros(x.shape[0], x.shape[1], x.shape[3], x.shape[2]*2, device=x.device)], dim=3)
        cc = cc.view(x.shape[0], x.shape[1], x.shape[3]*2, x.shape[2]*2)
        x_up = cc.permute(0,1,3,2)
        return 4 * self._conv_gauss(x_up)
    
    def _conv_dim3(self, x):
        return F.conv2d(x, self.kernel_dim3, groups=3)

    def _conv_dim1(self, x):
        return F.conv2d(x, self.kernel_dim1, groups=1)

    def _conv_gauss(self, img):
        channels = img.shape[1]
        return self._conv_dim3(F.pad(img, (2, 2, 2, 2), mode='reflect')) if channels == 3 else self._conv_dim1(F.pad(img, (2, 2, 2, 2), mode='reflect'))
    
    def laplacian_recon(self, laplacian_pyramid):
        recon = laplacian_pyramid[-1]
        pyramid_level = len(laplacian_pyramid)
        for i in range(pyramid_level - 1, 0, -1):
            up = self._upsample(recon)
            recon = up + laplacian_pyramid[i - 1]
        return recon
    
    def forward(self, img, pyramid_levels=3, mode='all'):
        '''
        guass_pyramid_size: 512(input image), 256, 128, 64
        laplacian_pyramid_size: 512, 256, 128, 64(minist image)
        '''
        img = img.to(self.device())
        if len(img.shape) == 3:
            img = img.unsqueeze(0)

        if mode == 'gauss':
            gauss_pyramid = []
            gauss_pyramid.append(img)
            for _ in range(pyramid_levels - 1):
                filtered = self._conv_gauss(img)
                down = self._downsample(filtered)
                gauss_pyramid.append(down)
                img = down
            return gauss_pyramid
        elif mode == 'laplacian':
            lap_pyramid = []
            for _ in range(pyramid_levels - 1):
                filtered = self._conv_gauss(img)
                down = self._downsample(filtered)
                up = self._upsample(down)
                diff = img - up
                lap_pyramid.append(diff)
                img = down
            lap_pyramid.append(img)
            return lap_pyramid
        elif mode == 'all':
            gauss_pyramid = []
            lap_pyramid = []
            gauss_pyramid.append(img)
            for _ in range(pyramid_levels - 1):
                filtered = self._conv_gauss(img)
                down = self._downsample(filtered)
                up = self._upsample(down)
                diff = img - up
                gauss_pyramid.append(down)
                lap_pyramid.append(diff)
                img = down
            lap_pyramid.append(img)
            return gauss_pyramid, lap_pyramid
        else:
            assert False, 'mode must be gauss, laplacian or all'