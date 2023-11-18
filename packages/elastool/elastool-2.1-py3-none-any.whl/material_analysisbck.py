import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from numpy import sin,cos,pi,tan,vstack, linalg
import plotly.graph_objects as go
from plotly.subplots import make_subplots

class MaterialAnalysis:

    def __init__(self, elastic_tensor, plot=False):
        if not (isinstance(elastic_tensor, np.ndarray) and 
                (elastic_tensor.shape == (3, 3) or elastic_tensor.shape == (6, 6))):
            raise ValueError("elastic_tensor must be a 3x3 matrix (for 2D) or a 6x6 matrix (for 3D).")

        
        self.C2d = elastic_tensor
        self.plot = plot
        self.S = linalg.inv(elastic_tensor)
        

    @property
    def v_2D(self):
        """
        return v_2D=C12/C22
        """
        return self.C2d[0][1]/self.C2d[1][1]

    @property
    def d1(self):
        """
        return d1=C11/C22+1-(C11*C22-C12**2)/C22/C66;
        """
        return self.C2d[0][0]/self.C2d[1][1]+1 - \
               (self.C2d[0][0]*self.C2d[1][1]-self.C2d[0][1]**2)/ \
               self.C2d[1][1]/self.C2d[2][2]

    @property
    def d2(self):
        """
        return d2=-(2*C12/C22-(C11*C22-C12**2)/C22/C66);
        """
        return -1*(2*self.C2d[0][1]/self.C2d[1][1]-\
                (self.C2d[0][0]*self.C2d[1][1]-self.C2d[0][1]**2)/ \
                 self.C2d[1][1]/self.C2d[2][2])

    @property
    def d3(self):
        """
        return d3 =C11/C22
        """
        return self.C2d[0][0]/self.C2d[1][1]

    @property
    def Y_2D(self):
        """
        return Y_2D = C11*C22-C12**2)/C22
        """
        return (self.C2d[0][0]*self.C2d[1][1]-self.C2d[0][1]**2)/self.C2d[1][1]

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
        numerator = self.C2d[2][2]
        denominator = 1 + (self.C2d[0][1] + self.C2d[2][2]) / (self.C2d[0][0] - self.C2d[0][1]) * tan(theta)**2
        G_theta = numerator / denominator
        return G_theta


    def compute_K_2D_polar(self, theta):
        K_theta = (self.C2d[0][0] + self.C2d[1][1] - 2*self.C2d[0][1] + 
                   (self.C2d[0][0] - self.C2d[0][1] - self.C2d[1][1]) * np.cos(2*theta)) / 2
        return K_theta


    def plot_orientation_dependent_2D(self, npoints=360, fname='EVGK_theta', dpi=80):
        theta = np.linspace(0, 2*np.pi, npoints)

        E = self.compute_E_2D_polar(theta)
        V = self.compute_V_2D_polar(theta)
        G = self.compute_G_2D_polar(theta)
        K = self.compute_K_2D_polar(theta)

        # Save the data
        data = np.vstack((theta, E, V, G, K)).T
        np.savetxt(f"{fname}.dat", data, fmt='%10.4f %10.4f %10.4f %10.4f %10.4f', header='Theta E V G K')

        sns.set_style("whitegrid")

        try:
            fig, axs = plt.subplots(2, 2, figsize=(12, 12), subplot_kw=dict(projection='polar'))

            # Young's Modulus
            axs[0, 0].plot(theta, E, color="tab:orange", lw=1, ls="--", marker='h', alpha=0.6, label="$E$")
            axs[0, 0].set_title("Young's Modulus")

            # Poisson's Ratio
            axs[0, 1].plot(theta, V, color="tab:green", lw=1, ls="--", marker='h', alpha=0.6, label="$\\nu$")
            axs[0, 1].set_title("Poisson's Ratio")

            # Shear Modulus
            axs[1, 0].plot(theta, G, color="tab:blue", lw=1, ls="--", marker='h', alpha=0.6, label="$G$")
            axs[1, 0].set_title("Shear Modulus")

            # Stiffness Constant
            axs[1, 1].plot(theta, K, color="tab:red", lw=1, ls="--", marker='h', alpha=0.6, label="$K$")
            axs[1, 1].set_title("Stiffness Constant")

            plt.tight_layout()
            plt.savefig(f"{fname}.png", format='png', dpi=dpi)
            plt.close(fig) 
            #plt.show()



            fig_plotly = make_subplots(rows=2, cols=2, subplot_titles=("Young's Modulus", "Poisson's Ratio", "Shear Modulus", "Stiffness Constant"), specs=[[{'type': 'polar'}, {'type': 'polar'}], [{'type': 'polar'}, {'type': 'polar'}]])

            # Add traces
            fig_plotly.add_trace(go.Scatterpolar(r=E, theta=theta*180/np.pi, name='E', marker=dict(symbol='circle')), 1, 1)
            fig_plotly.add_trace(go.Scatterpolar(r=V, theta=theta*180/np.pi, name='V', marker=dict(symbol='circle')), 1, 2)
            fig_plotly.add_trace(go.Scatterpolar(r=G, theta=theta*180/np.pi, name='G', marker=dict(symbol='circle')), 2, 1)
            fig_plotly.add_trace(go.Scatterpolar(r=K, theta=theta*180/np.pi, name='K', marker=dict(symbol='circle')), 2, 2)


            # Update layout
            fig_plotly.update_layout(title_text="Material Analysis")
            fig_plotly.write_image(f"{fname}plotly.png")  # Save the image
            fig_plotly.show()


        except Exception as e:
            print(f"Error while plotting: {e}")


# Sample usage
# st = Structure.from_file('POSCAR')
# c = np.random.randn(6,6) * 10
# c = c @ c.T
# analysis_instance = MaterialAnalysis(st, c, plot=True)
# analysis_instance.plot_orientation_dependent_values()


class MaterialAnalysis3D:


    def plot_orientation_dependent_3D_plotly(self, S, npoints=100, fname='EVGK_3D'):
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
        ])

        rho_e = self.compute_E_general(S, l)
        rho_v = self.compute_V_general(S, l)
        rho_g = self.compute_G_general(S, l)
        rho_k = self.compute_K_general(S, l)

        x_e, y_e, z_e = rho_e * np.sin(theta) * np.cos(phi), rho_e * np.sin(theta) * np.sin(phi), rho_e * np.cos(theta)
        x_v, y_v, z_v = rho_v * np.sin(theta) * np.cos(phi), rho_v * np.sin(theta) * np.sin(phi), rho_v * np.cos(theta)
        x_g, y_g, z_g = rho_g * np.sin(theta) * np.cos(phi), rho_g * np.sin(theta) * np.sin(phi), rho_g * np.cos(theta)
        x_k, y_k, z_k = rho_k * np.sin(theta) * np.cos(phi), rho_k * np.sin(theta) * np.sin(phi), rho_k * np.cos(theta)

        fig = go.Figure()

        fig.add_trace(go.Surface(z=z_e, x=x_e, y=y_e, colorscale='Viridis', cmin=0, cmax=np.amax(rho_e)))
        fig.add_trace(go.Surface(z=z_v, x=x_v, y=y_v, colorscale='Viridis', cmin=0, cmax=np.amax(rho_v)))
        fig.add_trace(go.Surface(z=z_g, x=x_g, y=y_g, colorscale='Viridis', cmin=0, cmax=np.amax(rho_g)))
        fig.add_trace(go.Surface(z=z_k, x=x_k, y=y_k, colorscale='Viridis', cmin=0, cmax=np.amax(rho_k)))

        fig.update_layout(title="3D Material Analysis", scene=dict(zaxis=dict(nticks=10, range=[np.amin(rho_e),np.amax(rho_e)])))

        fig.show()



    def plot_orientation_dependent_3D_with_sns(self, S, npoints=100, fname='EVGK_3D'):
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
        ])

        rho_e = self.compute_E_general(S, l)
        rho_v = self.compute_V_general(S, l)
        rho_g = self.compute_G_general(S, l)
        rho_k = self.compute_K_general(S, l)

        x_e, y_e, z_e = rho_e * np.sin(theta) * np.cos(phi), rho_e * np.sin(theta) * np.sin(phi), rho_e * np.cos(theta)
        x_v, y_v, z_v = rho_v * np.sin(theta) * np.cos(phi), rho_v * np.sin(theta) * np.sin(phi), rho_v * np.cos(theta)
        x_g, y_g, z_g = rho_g * np.sin(theta) * np.cos(phi), rho_g * np.sin(theta) * np.sin(phi), rho_g * np.cos(theta)
        x_k, y_k, z_k = rho_k * np.sin(theta) * np.cos(phi), rho_k * np.sin(theta) * np.sin(phi), rho_k * np.cos(theta)

        sns.set_style("whitegrid")
    
        fig = plt.figure(figsize=(12, 10))

        ax_e = fig.add_subplot(2, 2, 1, projection='3d')
        ax_e.plot_surface(x_e, y_e, z_e, cmap='viridis')
        ax_e.set_title("Young's Modulus")

        ax_v = fig.add_subplot(2, 2, 2, projection='3d')
        ax_v.plot_surface(x_v, y_v, z_v, cmap='viridis')
        ax_v.set_title("Poisson's Ratio")

        ax_g = fig.add_subplot(2, 2, 3, projection='3d')
        ax_g.plot_surface(x_g, y_g, z_g, cmap='viridis')
        ax_g.set_title("Shear Modulus")

        ax_k = fig.add_subplot(2, 2, 4, projection='3d')
        ax_k.plot_surface(x_k, y_k, z_k, cmap='viridis')
        ax_k.set_title("Bulk Modulus")

        plt.tight_layout()
        plt.show()



    def compute_E_3D_spherical(self, theta, phi):
        # Given constants for a cubic system (to be replaced with actual values)
        E = 210  # GPa (for example)
        nu = 0.3  # Poisson's ratio (for example)

        S_11 = (1 - nu) / E
        S_44 = 2 * (1 + nu) / E

        u = np.sin(theta) * np.cos(phi)
        v = np.sin(theta) * np.sin(phi)
        w = np.cos(theta)

        # Compute the orientation-dependent Young's modulus
        E_orientation = 1 / (S_11 / (u**4 + v**4 + w**4) + S_44 / (u**2 * v**2 + v**2 * w**2 + w**2 * u**2))

        return E_orientation


    def compute_V_3D_spherical(self, theta, phi):

        C_11 = 500  # GPa (for example)
        C_12 = 390  # GPa (for example)
        C_44 = 120  # GPa (for example)

        h = np.sin(theta) * np.cos(phi)
        k = np.sin(theta) * np.sin(phi)
        l = np.cos(theta)

        # Compute the orientation-dependent Poisson's ratio
        nu_orientation = (C_12 * h**2 + C_44 * (k**2 + l**2)) / (C_11 * h**2 + C_44 * (k**2 + l**2))

        return nu_orientation



    def compute_G_3D_spherical(self, theta, phi):
        # Given constants for a cubic system (replace with actual values)
        C_11 = 500  # GPa (for example)
        C_12 = 390  # GPa (for example)
        C_44 = 120  # GPa (for example)

        h = np.sin(theta) * np.cos(phi)
        k = np.sin(theta) * np.sin(phi)
        l = np.cos(theta)

        # Compute the orientation-dependent shear modulus
        G_orientation = (5 * (C_11 + C_12) * C_44) / (4 * C_44 + 3 * C_11 - 3 * C_12 - (C_11 - C_12) * (h**2 * k**2 + k**2 * l**2 + l**2 * h**2) / (h**2 * k**2 * l**2))

        return G_orientation




    def compute_K_3D_spherical(self, theta, phi):
    # Constants (replace with actual or desired values)
        K_0 = 250  # GPa (for example, average bulk modulus)
        K_1 = 50   # GPa (for example, amplitude of variation)
        m = 2     # Integer defining periodicity
    
        # Compute the orientation-dependent bulk modulus using our model
        K_orientation = K_0 + K_1 * np.sin(theta) * np.cos(m * phi)
    
        return K_orientation


    def plot_orientation_dependent_3Dold(self, npoints=100, fname='EVGK_3D'):
        theta = np.linspace(0, np.pi, npoints)
        phi = np.linspace(0, 2 * np.pi, npoints)

        theta, phi = np.meshgrid(theta, phi)
        rho_e = self.compute_E_3D_spherical(theta, phi)
        rho_v = self.compute_V_3D_spherical(theta, phi)
        rho_g = self.compute_G_3D_spherical(theta, phi)
        rho_k = self.compute_K_3D_spherical(theta, phi)

        x_e, y_e, z_e = rho_e * np.sin(theta) * np.cos(phi), rho_e * np.sin(theta) * np.sin(phi), rho_e * np.cos(theta)
        x_v, y_v, z_v = rho_v * np.sin(theta) * np.cos(phi), rho_v * np.sin(theta) * np.sin(phi), rho_v * np.cos(theta)
        x_g, y_g, z_g = rho_g * np.sin(theta) * np.cos(phi), rho_g * np.sin(theta) * np.sin(phi), rho_g * np.cos(theta)
        x_k, y_k, z_k = rho_k * np.sin(theta) * np.cos(phi), rho_k * np.sin(theta) * np.sin(phi), rho_k * np.cos(theta)

        fig = go.Figure()

        fig.add_trace(go.Surface(z=z_e, x=x_e, y=y_e, colorscale='Viridis', cmin=0, cmax=np.amax(rho_e)))
        fig.add_trace(go.Surface(z=z_v, x=x_v, y=y_v, colorscale='Viridis', cmin=0, cmax=np.amax(rho_v)))
        fig.add_trace(go.Surface(z=z_g, x=x_g, y=y_g, colorscale='Viridis', cmin=0, cmax=np.amax(rho_g)))
        fig.add_trace(go.Surface(z=z_k, x=x_k, y=y_k, colorscale='Viridis', cmin=0, cmax=np.amax(rho_k)))

        fig.update_layout(title="3D Material Analysis", scene=dict(zaxis=dict(nticks=10, range=[np.amin(rho_e),np.amax(rho_e)])))

        fig.show()








def uvw_to_l():
    """
    Converts the [uvw] direction to the six-component vector l for cubic symmetry.
    
    Parameters:
    - u, v, w: Crystallographic direction [uvw]
    
    Returns:
    - l: six-component direction vector
    """

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
    ])
    
    return l

def compute_E_general(S):
    """
    Compute the orientation-dependent modulus E_uvw based on the compliance matrix S and direction [uvw].
    
    Parameters:
    - S: 6x6 compliance matrix
    - u, v, w: Crystallographic direction [uvw]
    
    Returns:
    - E_uvw: orientation-dependent modulus
    """
    l = uvw_to_l()
    E_inv = sum(S[i, j] * l[i] * l[j] for i in range(6) for j in range(6))
    return 1.0 / E_inv



def compute_V_general(E_uvw, G_uvw):
    """
    Compute the orientation-dependent Poisson's ratio nu_uvw based on E_uvw and G_uvw.
    
    Returns:
    - nu_uvw: orientation-dependent Poisson's ratio
    """
    return E_uvw / (2 * G_uvw) - 1

def compute_G_general(S, l):
    """
    Compute the orientation-dependent shear modulus G_uvw based on the compliance matrix S and direction l.
    
    Returns:
    - G_uvw: orientation-dependent shear modulus
    """
    l = uvw_to_l()
    G_inv = sum(l[i] * l[j] * l[k] * l[m] * S[i, j, k, m] for i in range(6) for j in range(6) for k in range(6) for m in range(6))
    return 1.0 / G_inv


def compute_K_general(S):
    """
    Compute the orientation-dependent bulk modulus K_uvw based on the compliance matrix S and direction l.
    
    Returns:
    - K_uvw: orientation-dependent bulk modulus
    """
    l = uvw_to_l()
    K_inv = sum(l[i] * l[j] * S[i, j] for i in range(6) for j in range(6))
    return 1.0 / K_inv

