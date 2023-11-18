import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from numpy import sin,cos,pi,tan,vstack, linalg
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from matplotlib.colors import PowerNorm
import matplotlib.colors as mcolors


class MaterialAnalysis:

    def __init__(self, elastic_tensor, plot=False, plotly=False):
        if not (isinstance(elastic_tensor, np.ndarray) and 
                (elastic_tensor.shape == (3, 3) or elastic_tensor.shape == (6, 6))):
            raise ValueError("elastic_tensor must be a 3x3 matrix (for 2D) or a 6x6 matrix (for 3D).")

        
        self.Cdim = elastic_tensor
        self.plot = plot
        self.Cs = linalg.inv(elastic_tensor)
        self.plotly = plotly
        

    @property
    def v_2D(self):
        """
        return v_2D=C12/C22
        """
        return self.Cdim[0][1]/self.Cdim[1][1]

    @property
    def d1(self):
        """
        return d1=C11/C22+1-(C11*C22-C12**2)/C22/C66;
        """
        return self.Cdim[0][0]/self.Cdim[1][1]+1 - \
               (self.Cdim[0][0]*self.Cdim[1][1]-self.Cdim[0][1]**2)/ \
               self.Cdim[1][1]/self.Cdim[2][2]

    @property
    def d2(self):
        """
        return d2=-(2*C12/C22-(C11*C22-C12**2)/C22/C66);
        """
        return -1*(2*self.Cdim[0][1]/self.Cdim[1][1]-\
                (self.Cdim[0][0]*self.Cdim[1][1]-self.Cdim[0][1]**2)/ \
                 self.Cdim[1][1]/self.Cdim[2][2])


    def print_Cs(self):
        print("Compliance matrix (Cs):")
        print(self.Cs)


    @property
    def d3(self):
        """
        return d3 =C11/C22
        """
        return self.Cdim[0][0]/self.Cdim[1][1]

    @property
    def Y_2D(self):
        """
        return Y_2D = C11*C22-C12**2)/C22
        """
        return (self.Cdim[0][0]*self.Cdim[1][1]-self.Cdim[0][1]**2)/self.Cdim[1][1]

    def compute_E_2D_polar(self, theta):
        denominator = cos(theta)**4 + self.d2 * cos(theta)**2 * sin(theta)**2 + self.d3 * sin(theta)**4
        E_theta = self.Y_2D / denominator
        return E_theta

    def compute_V_2D_polar(self, theta):
        numerator = self.v_2D * cos(theta)**4 - self.d1 * cos(theta)**2 * sin(theta)**2 + self.v_2D * sin(theta)**4
        denominator = cos(theta)**4 + self.d2 * cos(theta)**2 * sin(theta)**2 + self.d3 * sin(theta)**4
        V_theta = numerator / denominator
        return V_theta

    #As per the 3 x 3 nature of 2D materials' elastic tensor, 55 => 33
    def compute_G_2D_polar(self, theta):
        numerator = self.Cdim[2][2]
        denominator = 1 + (self.Cdim[0][1] + self.Cdim[2][2]) / (self.Cdim[0][0] - self.Cdim[0][1]) * tan(theta)**2
        G_theta = numerator / denominator
        return G_theta


    def compute_K_2D_polar(self, theta):
        K_theta = (self.Cdim[0][0] + self.Cdim[1][1] - 2*self.Cdim[0][1] + 
                   (self.Cdim[0][0] - self.Cdim[0][1] - self.Cdim[1][1]) * np.cos(2*theta)) / 2
        return K_theta



    def uvw_to_l(self):
        """
        Converts the [uvw] direction to the six-component vector l for cubic symmetry.
    
        Parameters:
        - u, v, w: Crystallographic direction [uvw]
    
        Returns:
        - l: six-component direction vector
        """
        npoints = 360
        theta = np.linspace(0, np.pi, npoints)
        phi = np.linspace(0, 2 * np.pi, npoints)

        theta, phi = np.meshgrid(theta, phi)

        u = np.sin(theta) * np.cos(phi)
        v = np.sin(theta) * np.sin(phi)
        w = np.cos(theta)
    
        # Normalize the [uvw] direction
        #norm = np.sqrt(u**2 + v**2 + w**2)
        #u /= norm
        #v /= norm
        #w /= norm

        # Convert [uvw] to the six-component vector l
        l = np.array([
            u**2,
            v**2,
            w**2,
            2*u*v,
            2*v*w,
            2*u*w
        ]).transpose(1, 2, 0)
    
        return l


    def adjust_colormap_brightness(self,cmap_name, scale_factor):
        cmap = plt.get_cmap(cmap_name)
        colors = cmap(np.arange(cmap.N))


    def compute_E_general(self,l):
        """
        Compute the orientation-dependent modulus E_uvw based on the compliance matrix S and direction [uvw].
    
        Parameters:
        - S: 6x6 compliance matrix
        - u, v, w: Crystallographic direction [uvw]
    
        Returns:
        - E_uvw: orientation-dependent modulus
        """
        #l = self.uvw_to_l()
        E_inv = sum(self.Cs[i, j] * l[i] * l[j] for i in range(6) for j in range(6))
        return 1.0 / E_inv



#    def compute_G_general(self,l):
#        """
#        Compute the orientation-dependent shear modulus G_uvw based on the compliance matrix S and direction l.
#    
#        Returns:
#        - G_uvw: orientation-dependent shear modulus
#        """
#        #l = self.uvw_to_l()
#        G_inv = sum(l[i] * l[j] * l[k] * l[m] * self.Cs[i, j, k, m] for i in range(6) for j in range(6) for k in range(6) for m in range(6))
#        print(f"For l: {l}, G_inv is: {1./G_inv}")
#        return 1.0 / G_inv


    def compute_G_general(self, l):
        # Mapping from Voigt notation to 4D tensor indices
        voigt_to_tensor_mapping = {
            0: (0, 0),
            1: (1, 1),
            2: (2, 2),
            3: (1, 2),
            4: (0, 2),
            5: (0, 1)
        }

        G_inv = 0
        for i in range(6):
            for j in range(6):
                tensor_i = voigt_to_tensor_mapping[i]
                tensor_j = voigt_to_tensor_mapping[j]
                G_inv += l[tensor_i[0]] * l[tensor_i[1]] * l[tensor_j[0]] * l[tensor_j[1]] * self.Cs[i, j]

        #print(f"For l: {l}, G_inv is: {G_inv}")
    
        if G_inv == 0:
          #  print("G_inv is zero!")
            return float('inf')  # or handle this case appropriately

        return 1.0 / G_inv

    def compute_V_general(self,l):
        """
        Compute the orientation-dependent Poisson's ratio nu_uvw based on E_uvw and G_uvw.
    
        Returns:
        - nu_uvw: orientation-dependent Poisson's ratio
        """
        E_uvw = self.compute_E_general(l)
        G_uvw = self.compute_G_general(l)
        return E_uvw / (2 * G_uvw) - 1


    def compute_K_general(self,l):
        """
        Compute the orientation-dependent bulk modulus K_uvw based on the compliance matrix S and direction l.
    
        Returns:
        - K_uvw: orientation-dependent bulk modulus
        """
       # l = self.uvw_to_l()
        K_inv = sum(l[i] * l[j] * self.Cs[i, j] for i in range(6) for j in range(6))
        return 1.0 / K_inv


    def compute_moduli_contour_2D(self, theta, phi):
        epsilon = 1e-8  # Small regularizing constant

        C11, C12, C16, _, C22, C26, _, _, C66 = self.Cdim.ravel()
        
        x = np.sin(theta) * np.cos(phi)
        y = np.sin(theta) * np.sin(phi)

        # Modified stiffness constants
        C11_prime = C11 * x**4 + C22 * y**4 + 2 * (C12 + 2 * C66) * x**2 * y**2 + 4 * (C16 * x**3 * y + C26 * x * y**3)
        C22_prime = C11 * y**4 + C22 * x**4 + 2 * (C12 + 2 * C66) * x**2 * y**2 + 4 * (C16 * x * y**3 + C26 * x**3 * y)
        C12_prime = (C11 + C22 - 4 * C66) * x**2 * y**2 + C12 * (x**4 + y**4) + 2 * (C16 * x * (x**2 - y**2) + C26 * y * (y**2 - x**2))
        C66_prime = (C11 + C22 - 2 * C12) * x**2 * y**2 + C66 * (x**4 + y**4) + 2 * (C16 - C26) * x * y * (x**2 - y**2)

        # Calculate compliance values
        S11_prime = 1 / (C11_prime + epsilon)
        S22_prime = 1 / (C22_prime + epsilon)
        S66_prime = 1 / (C66_prime + epsilon)

        # Compute S12_prime, guarding against division by zero
        denominator = C11_prime * C22_prime - C12_prime**2
        S12_prime = np.where(np.abs(denominator) < epsilon, 0.0, -C12_prime / denominator)

        # Calculate moduli
        Ex = 1 / S11_prime
        Ey = 1 / S22_prime
        Gxy = 1 / S66_prime

        # Poisson's ratios
        nu_xy = -S12_prime * S11_prime
        nu_yx = -S12_prime * S22_prime

        # Stiffness constant
        K_prime = (C11_prime + C22_prime + 2 * C12_prime) / 3

        return Ex, Ey, Gxy, nu_xy, nu_yx, K_prime


    # Transform the stiffness matrix
    def transform_stiffness_3D(self, theta, phi):
        # Extract the 3x3 submatrix
        C_sub = self.Cdim[:3, :3]

        # Transformation matrix
        M = np.array([
            [np.sin(theta) * np.cos(phi), np.sin(theta) * np.sin(phi), np.cos(theta)],
            [np.cos(theta) * np.cos(phi), np.cos(theta) * np.sin(phi), -np.sin(theta)],
            [-np.sin(phi), np.cos(phi), 0]
        ])
        return M @ C_sub @ M.T


    def safe_inverse(self,value, tol=1e-5):
        """Returns inverse if value is not too close to zero; otherwise returns infinity."""
        if np.isclose(value, 0, atol=tol):
            return np.inf
        else:
            return 1 / value



    # Compute directional moduli for 3D material
    def compute_moduli_directional_3D(self,Sij):
        #Sij = self.Cs

        # Young's moduli
        E1 = 1 / Sij[0, 0]
        E2 = 1 / Sij[1, 1]
        E3 = 1 / Sij[2, 2]

        # Shear moduli
        G23 = 1 / Sij[1, 2]
        G13 = 1 / Sij[0, 2]
        G12 = 1 / Sij[0, 1]

        # Poisson's ratios
        nu12 = -Sij[0, 1] * Sij[0, 0]
        nu21 = -Sij[1, 0] * Sij[1, 1]
        nu13 = -Sij[0, 2] * Sij[0, 0]
        nu31 = -Sij[2, 0] * Sij[2, 2]
        nu23 = -Sij[1, 2] * Sij[1, 1]
        nu32 = -Sij[2, 1] * Sij[2, 2]

        # Bulk modulus
        K = 1 / (Sij[0, 0] + 2 * Sij[0, 1])

        return E1, E2, E3, G23, G13, G12, nu12, nu21, nu13, nu31, nu23, nu32, K



    def transform_stiffness_2D(self, theta):
        # 2D transformation matrix for anisotropic plane strain
        C_sub = self.Cdim[:3, :3]
        M = np.array([
            [np.cos(theta), np.sin(theta), 0],
            [-np.sin(theta), np.cos(theta), 0],
            [0, 0, 1]
        ])
        return M @ C_sub @ M.T

    def compute_moduli_directional_2D(self, Sij):
        threshold = 1e-3
        close_to_zero_mask = np.abs(Sij) < threshold
        Sij[close_to_zero_mask] = 0
        # Young's moduli
        E1 = 1 / Sij[0, 0]
        E2 = 1 / Sij[1, 1]

        # Shear moduli
        G12 = 1 / self.safe_inverse(Sij[0, 1])
        G23 = 1 / self.safe_inverse(Sij[1, 2])
        G13 = 1 / self.safe_inverse(Sij[0, 2])

        # Poisson's ratios
        nu12 = -Sij[0, 1] * Sij[0, 0]
        nu21 = -Sij[1, 0] * Sij[1, 1]
        nu13 = -Sij[0, 2] * Sij[0, 0]
        nu31 = -Sij[2, 0] * Sij[2, 2]
        nu23 = -Sij[1, 2] * Sij[1, 1]
        nu32 = -Sij[2, 1] * Sij[2, 2]

        return E1, E2, G12, G23, G13, nu12, nu21, nu13, nu31, nu23, nu32





    def plot_orientation_dependent_2D(self, npoints=360, fname='EVGK_polar_2D', dpi=80):
        theta = np.linspace(0, 2*np.pi, npoints)

        E = self.compute_E_2D_polar(theta)
        V = self.compute_V_2D_polar(theta)
        G = self.compute_G_2D_polar(theta)
        K = self.compute_K_2D_polar(theta)

        # Save the data
        data = np.vstack((theta, E, V, G, K)).T
        np.savetxt(f"{fname}.dat", data, fmt='%10.4f %10.4f %10.4f %10.4f %10.4f', header='Theta E V G K')


        # Set global style parameters
        plt.rcParams.update({'font.size': 16, 'font.family': 'sans-serif'})

        sns.set_style("whitegrid")

        try:
            fig, axs = plt.subplots(2, 2, figsize=(12, 12), subplot_kw=dict(projection='polar'))

            # Define line properties
            line_properties = {'lw': 2, 'ls': '-', 'alpha': 0.7}

            # Young's Modulus
            axs[0, 0].plot(theta, E, color="tab:orange", marker='o', label="$E$", **line_properties)
            axs[0, 0].set_title("Young's Modulus", fontsize=16)

            # Poisson's Ratio
            axs[0, 1].plot(theta, V, color="tab:green", marker='o', label="$\\nu$", **line_properties)
            axs[0, 1].set_title("Poisson's Ratio", fontsize=16)

            # Shear Modulus
            axs[1, 0].plot(theta, G, color="tab:blue", marker='o', label="$G$", **line_properties)
            axs[1, 0].set_title("Shear Modulus", fontsize=16)

            # Stiffness Constant
            axs[1, 1].plot(theta, K, color="tab:red", marker='o', label="$K$", **line_properties)
            axs[1, 1].set_title("Stiffness Constant", fontsize=16)

            plt.tight_layout()
            plt.savefig(f"{fname}.png", format='png', dpi=dpi)
            plt.close(fig) 


            if self.plotly:
                fig_plotly = make_subplots(rows=2, cols=2, subplot_titles=("Young's Modulus", "Poisson's Ratio", "Shear Modulus", "Stiffness Constant"), specs=[[{'type': 'polar'}, {'type': 'polar'}], [{'type': 'polar'}, {'type': 'polar'}]])
                fig_plotly.update_layout(
                    title_text="Material Analysis with ElasTool",
                    font=dict(size=12, family='sans-serif')
                )

                # Add traces
                fig_plotly.add_trace(go.Scatterpolar(r=E, theta=theta*180/np.pi, name='E', marker=dict(symbol='circle')), 1, 1)
                fig_plotly.add_trace(go.Scatterpolar(r=V, theta=theta*180/np.pi, name='V', marker=dict(symbol='circle')), 1, 2)
                fig_plotly.add_trace(go.Scatterpolar(r=G, theta=theta*180/np.pi, name='G', marker=dict(symbol='circle')), 2, 1)
                fig_plotly.add_trace(go.Scatterpolar(r=K, theta=theta*180/np.pi, name='K', marker=dict(symbol='circle')), 2, 2)


                # Update layout
                fig_plotly.update_layout(title_text="Material Analysis with ElasTool")
                fig_plotly.write_image(f"{fname}plotly.png")  # Save the image
                fig_plotly.show()


        except Exception as e:
            print(f"Error while plotting: {e}")


    def plot_orientation_dependent_3D(self, npoints=360, fname='EVGK_polar_3D',dpi = 80):
        theta = np.linspace(0, np.pi, npoints)
        phi = np.linspace(0, 2 * np.pi, npoints)

        theta, phi = np.meshgrid(theta, phi)

        u = np.sin(theta) * np.cos(phi)
        v = np.sin(theta) * np.sin(phi)
        w = np.cos(theta)
        l = np.array([
            u**2,
            v**2,
            w**2,
            2*u*v,
            2*v*w,
            2*u*w
        ]).transpose(1, 2, 0)

        rho_e = np.empty_like(theta)
        rho_v = np.empty_like(theta)
        rho_g = np.empty_like(theta)
        rho_k = np.empty_like(theta)

 
        for i in range(npoints):
            for j in range(npoints):
                l_point = l[i, j, :]  # Extract the 6-component vector at this point
                rho_e[i, j] = self.compute_E_general(l_point)
                rho_v[i, j] = self.compute_V_general(l_point)
                rho_g[i, j] = self.compute_G_general(l_point)
                rho_k[i, j] = self.compute_K_general(l_point)



        x_e, y_e, z_e = rho_e * np.sin(theta) * np.cos(phi), rho_e * np.sin(theta) * np.sin(phi), rho_e * np.cos(theta)
        x_v, y_v, z_v = rho_v * np.sin(theta) * np.cos(phi), rho_v * np.sin(theta) * np.sin(phi), rho_v * np.cos(theta)
        x_g, y_g, z_g = rho_g * np.sin(theta) * np.cos(phi), rho_g * np.sin(theta) * np.sin(phi), rho_g * np.cos(theta)
        x_k, y_k, z_k = rho_k * np.sin(theta) * np.cos(phi), rho_k * np.sin(theta) * np.sin(phi), rho_k * np.cos(theta)

        sns.set_style("whitegrid")
        plt.rcParams.update({'font.size': 16, 'font.family': 'sans-serif'})
        try:    
            fig = plt.figure(figsize=(12, 10))

            ax_e = fig.add_subplot(2, 2, 1, projection='3d')
            ax_e.plot_surface(x_e, y_e, z_e, cmap='viridis')
            ax_e.set_title("Young's Modulus",fontsize=16)

            ax_e.set_xlabel('X')
            ax_e.set_ylabel('Y')
            ax_e.set_zlabel('Z')

            ax_v = fig.add_subplot(2, 2, 2, projection='3d')
            ax_v.plot_surface(x_v, y_v, z_v, cmap='viridis')
            ax_v.set_title("Poisson's Ratio",fontsize=16)

            ax_v.set_xlabel('X')
            ax_v.set_ylabel('Y')
            ax_v.set_zlabel('Z')

            ax_g = fig.add_subplot(2, 2, 3, projection='3d')
            ax_g.plot_surface(x_g, y_g, z_g, cmap='viridis')
            ax_g.set_title("Shear Modulus",fontsize=16)

            ax_g.set_xlabel('X')
            ax_g.set_ylabel('Y')
            ax_g.set_zlabel('Z')

            ax_k = fig.add_subplot(2, 2, 4, projection='3d')
            ax_k.plot_surface(x_k, y_k, z_k, cmap='viridis')
            ax_k.set_title("Bulk Modulus",fontsize=16)

            ax_k.set_xlabel('X')
            ax_k.set_ylabel('Y')
            ax_k.set_zlabel('Z')

            plt.tight_layout()
            plt.savefig(f"{fname}.png", format='png', dpi=dpi)
            plt.close(fig) 
            #plt.show()

            if self.plotly:


                fig_plotly = make_subplots(
                    rows=2, cols=2,
                    specs=[[{'type': 'surface'}, {'type': 'surface'}],
                    [{'type': 'surface'}, {'type': 'surface'}]],
                    subplot_titles=('Young\'s Modulus', 'Poisson\'s Ratio', 'Shear Modulus', 'Bulk Modulus')
                   )

                # Young's Modulus plot
                fig_plotly.add_trace(
                   go.Surface(z=z_e, x=x_e, y=y_e, colorscale='Viridis', showscale=False),
                   row=1, col=1
                )

                # Poisson's Ratio plot
                fig_plotly.add_trace(
                    go.Surface(z=z_v, x=x_v, y=y_v, colorscale='Viridis', showscale=False),
                    row=1, col=2
                )

                # Shear Modulus plot
                fig_plotly.add_trace(
                    go.Surface(z=z_g, x=x_g, y=y_g, colorscale='Viridis', showscale=False),
                    row=2, col=1
                )

                # Bulk Modulus plot
                fig_plotly.add_trace(
                    go.Surface(z=z_k, x=x_k, y=y_k, colorscale='Viridis', showscale=False),
                    row=2, col=2
                )

                # Update layouts and axes titles
                fig_plotly.update_layout(scene=dict(xaxis_title='X', yaxis_title='Y', zaxis_title='Z'),
                           scene2=dict(xaxis_title='X', yaxis_title='Y', zaxis_title='Z'),
                           scene3=dict(xaxis_title='X', yaxis_title='Y', zaxis_title='Z'),
                           scene4=dict(xaxis_title='X', yaxis_title='Y', zaxis_title='Z'),
                           margin=dict(l=0, r=0, b=40, t=40),
                           title_text="Material Analysis with ElasTool")

                fig_plotly.write_image(f"{fname}plotly.png")
                fig_plotly.show()

        except Exception as e:
            print(f"Error while plotting: {e}")



    def plot_contour_2D(self,npoints=200, fname='EVGK_contour_2D',dpi = 200):

        norm = PowerNorm(0.75)  # gamma value, which you can adjust


        theta = np.linspace(0, np.pi, npoints)
        phi = np.linspace(0, 2*np.pi, npoints)
        Theta, Phi = np.meshgrid(theta, phi)

        Ex, Ey, Gxy, nu_xy, nu_yx, K = self.compute_moduli_contour_2D(Theta, Phi)


        try:
            fig, axes = plt.subplots(3, 2, figsize=(10, 10)) #,subplot_kw=dict(projection='polar'))

            for ax in axes.ravel():
                ax.set_facecolor('white')
           # for i in range(3):
           #     for j in range(2):
           #         axes[i, j].set_theta_direction(-1)  # Clockwise
           #         axes[i, j].set_theta_offset(np.pi)  # Starting from the top

            # Young's Modulus Ex
            brighten_color = self.adjust_colormap_brightness('rainbow', 0.05)
            colormap_obj = plt.get_cmap(brighten_color)
            levels = 50
            contour1 = axes[0, 0].contourf(Theta, Phi, Ex, cmap=colormap_obj, levels=levels,norm=norm)
            fig.colorbar(contour1, ax=axes[0, 0], label="Young's Modulus Ex")
            axes[0, 0].set_title("Young's Modulus Ex")
            axes[0, 0].set_xlabel('θ')
            axes[0, 0].set_ylabel('φ')

            # Young's Modulus Ey
            contour2 = axes[0, 1].contourf(Theta, Phi, Ey, cmap=colormap_obj, levels=levels)
            fig.colorbar(contour2, ax=axes[0, 1], label="Young's Modulus Ey")
            axes[0, 1].set_title("Young's Modulus Ey")
            axes[0, 1].set_xlabel('θ')
            axes[0, 1].set_ylabel('φ')

            # Shear Modulus Gxy
            contour3 = axes[1, 0].contourf(Theta, Phi, Gxy, cmap=colormap_obj, levels=levels)
            fig.colorbar(contour3, ax=axes[1, 0], label="Shear Modulus Gxy")
            axes[1, 0].set_title("Shear Modulus Gxy")
            axes[1, 0].set_xlabel('θ')
            axes[1, 0].set_ylabel('φ')

            #levels_nu = np.linspace(nu_xy.min(), nu_xy.max(), levels)

            # Poisson's Ratio νxy
            contour4 = axes[1, 1].contourf(Theta, Phi, nu_xy, cmap=colormap_obj, levels=levels)
            fig.colorbar(contour4, ax=axes[1, 1], label="Poisson's Ratio νxy")
            axes[1, 1].set_title("Poisson's Ratio νxy")
            axes[1, 1].set_xlabel('θ')
            axes[1, 1].set_ylabel('φ')

            # Bulk Modulus K
            contour5 = axes[2, 0].contourf(Theta, Phi, K, cmap=colormap_obj, levels=levels)
            fig.colorbar(contour5, ax=axes[2, 0], label="Bulk Modulus K")
            axes[2, 0].set_title("Bulk Modulus K")
            axes[2, 0].set_xlabel('θ')
            axes[2, 0].set_ylabel('φ')
 
            # Poisson's Ratio νyx
            contour6 = axes[2, 1].contourf(Theta, Phi, nu_yx, cmap=colormap_obj, levels=levels)
            fig.colorbar(contour6, ax=axes[2, 1], label="Poisson's Ratio νyx")
            axes[2, 1].set_title("Poisson's Ratio νyx")
            axes[2, 1].set_xlabel('θ')
            axes[2, 1].set_ylabel('φ')

            plt.tight_layout(pad=2.0)
            #plt.show()

            plt.savefig(f"{fname}.png", format='png', dpi=dpi,facecolor=fig.get_facecolor())
            plt.close(fig) 

        except Exception as e:
            print(f"Error while plotting 2D contour: {e}")



    def plot_contour_polar_3D(self,npoints=200, fname='EVGK_polar_contour_3D',dpi = 200):

        theta = np.linspace(0, np.pi, npoints)
        phi = np.linspace(0, 2*np.pi, npoints)
        Theta, Phi = np.meshgrid(theta, phi)

        # Calculate the transformed stiffness matrix and moduli
        C_prime = np.array([self.transform_stiffness_3D(t, p) for t, p in zip(np.ravel(Theta), np.ravel(Phi))])
        moduli = np.array([self.compute_moduli_directional_3D(np.linalg.inv(cp)) for cp in C_prime])


#moduli = np.array([self.compute_moduli_directional_3D(np.linalg.inv(cp)) for cp in C_prime])

        try:
            # Visualization
            fig, axes = plt.subplots(5, 3, figsize=(15, 20), subplot_kw={'projection': 'polar'})

      
            titles = [
                ["Young's Modulus E1", "Young's Modulus E2", "Young's Modulus E3"],
                ["Shear Modulus G23", "Shear Modulus G13", "Shear Modulus G12"],
                ["Poisson's Ratio ν12", "Poisson's Ratio ν21", "Poisson's Ratio ν13"],
                ["Poisson's Ratio ν31", "Poisson's Ratio ν23", "Poisson's Ratio ν32"],
                ["Bulk Modulus K", "", ""]
            ]
            E1, E2, E3, G23, G13, G12, nu12, nu21, nu13, nu31, nu23, nu32, K = [x.reshape(Theta.shape) for x in moduli.T]
            data = [E1, E2, E3, G23, G13, G12, nu12, nu21, nu13, nu31, nu23, nu32, K]
            levels = 10
            for i in range(5):
                for j in range(3):
                    if titles[i][j]:  # Only plot if there's a title
                        c = axes[i][j].contourf(Phi, Theta, data[i*3 + j], cmap='coolwarm', levels=levels)
                        axes[i][j].set_title(titles[i][j])
                        fig.colorbar(c, ax=axes[i][j])
                        contours = axes[i][j].contour(Phi, Theta, data[i*3 + j], levels=2, colors='black')
                        plt.clabel(contours, inline=True, fontsize=8)
                    else:
                        axes[i][j].set_visible(False)  # Hide unused subplots


            plt.tight_layout()
            #plt.show()

            plt.savefig(f"{fname}.png", format='png', dpi=dpi)
            plt.close(fig) 
#            if self.plotly:
#                # Create a subplot structure
#                pltplotly = make_subplots(rows=5, cols=3, subplot_titles=[title for sublist in titles for title in sublist])
#
#                for i in range(5):
#                    for j in range(3):
#                        if titles[i][j]:  # Only plot if there's a title
#                            pltplotly.add_trace(go.Contour(
#                               z=data[i*3 + j], 
#                               x=Phi[0],  # Assuming Phi and Theta are grids, so we take the 1D arrays
#                               y=Theta[:, 0],
#                               colorscale='RdBu',  # Analogous to 'coolwarm' in matplotlib
#                               contours=dict(start=np.min(data[i*3 + j]), end=np.max(data[i*3 + j]), size=(np.max(data[i*3 + j])-np.min(data[i*3 + j]))/levels, coloring='fill', showlines=True),
#                             line=dict(width=0.5, color='black')
#                    ), row=i+1, col=j+1)
#
#                # Update layout to fit titles and adjust any other aesthetic properties
#                pltplotly.update_layout(title_text="Contour Plots", showlegend=False)
#
#                # Show the plot
#                #pltplotly.show()
#                pltplotly.write_image(f"{fname}plotly.png")



        except Exception as e:
            print(f"Error while plotting 3D contour: {e}")




    def plot_contour_polar_2D(self, npoints=200, fname='EVGK_polar_contour_2D', dpi=200):
        theta_values = np.linspace(0, 2 * np.pi, npoints)
        radius = np.array([0, 1])

        # Calculate the transformed stiffness matrix and moduli
        C_prime = np.array([self.transform_stiffness_2D(t) for t in theta_values])

        moduli = []
        for cp in C_prime:
            # Check determinant
            det = np.linalg.det(cp)
            if np.abs(det) < 1e-10:
                print(f"Warning: Matrix is close to singular with determinant {det}")

            # Check condition number
            cond_num = np.linalg.cond(cp)
            if cond_num > 1e12:  # Adjust the threshold based on your context
                print(f"Warning: Matrix is ill-conditioned with condition number {cond_num}")
            
            alpha = 1e-5
            cp += alpha * np.eye(cp.shape[0])

            # Safe inversion using pseudo-inverse
            Sij = np.linalg.pinv(cp)

            # Compute the moduli for this orientation
            mod_values = self.compute_moduli_directional_2D(Sij)
            moduli.append(mod_values)

        moduli = np.array(moduli)


        # Visualization
        titles = [
            "Young's Modulus E1", "Young's Modulus E2", "Shear Modulus G12",
            "Shear Modulus G13","Shear Modulus G23", "Poisson's Ratio ν12",
            "Poisson's Ratio ν21", "Poisson's Ratio ν13","Poisson's Ratio ν23"
        ]
        fig, axes = plt.subplots(2, 4, figsize=(15, 8), subplot_kw={'projection': 'polar'})

        theta, radius = np.meshgrid(theta_values, radius)

        levels = 50
        for i, ax in enumerate(axes.ravel()):
            if i < len(titles):
                z_data = np.tile(moduli[:, i], (2,1))

                c = ax.contourf(theta, radius, z_data, cmap='rainbow', levels=levels)
                ax.set_title(titles[i])

                try:
                    fig.colorbar(c, ax=ax)
                except ValueError as e:
                    print(f"Failed to create colorbar for plot {i}. Error: {e}")


                #fig.colorbar(c, ax=ax)
                contours = ax.contour(theta, radius, z_data, levels=2, colors='black')
                plt.clabel(contours, inline=True, fontsize=8)
            else:
                ax.set_visible(False)  # Hide unused subplots

        plt.tight_layout()
        plt.savefig(f"{fname}.png", format='png', dpi=dpi)
        plt.close(fig)
        #plt.show()






