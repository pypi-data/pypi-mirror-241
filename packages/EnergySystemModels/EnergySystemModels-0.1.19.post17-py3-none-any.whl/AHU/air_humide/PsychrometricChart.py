import matplotlib.pyplot as plt
import numpy as np
from AHU.air_humide import air_humide

class Object:
    def __init__(self):
        self.T_db_range_max=40
        self.T_db_range_min=-10
        self.title='Diagramme Psychrométrique'
        self.T_db_range = np.linspace(self.T_db_range_min, self.T_db_range_max, self.T_db_range_max-self.T_db_range_min)  # Températures de -10 à 40°C
        self.max_w_value = air_humide.func_w(T_db=40, RH=100)  # Valeur maximale de w à 40°C et 100% d'humidité relative
        self.RH_values_dizaines = list(range(10, 101, 10))  # 10, 20, ..., 100
        self.RH_values_intermediaires = list(range(5, 96, 10))  # 5, 15, ..., 95
        self.enthalpy_values = list(range(0, 111, 10))  # Entalpies souhaitées en kJ/kg
        self.fig, self.ax = plt.subplots(figsize=(10, 6))
        self._plot_base_chart()

    def set_title(self, new_title):
        self.title = new_title
        self.ax.set_title(self.title)
         
    def set_x_max(self,x_max):
        self.T_db_range_max=x_max

    def _plot_base_chart(self):
        for RH in self.RH_values_dizaines + self.RH_values_intermediaires:
            w_values = [air_humide.func_w(RH=RH, T_db=T_db) for T_db in self.T_db_range]
            line_style = 'k-' if RH % 10 == 0 else 'k--'
            self.ax.plot(self.T_db_range, w_values, line_style, linewidth=0.5)

        for h_value in self.enthalpy_values:
            w_values = [air_humide.func_w(h=h_value, T_db=T_db) for T_db in self.T_db_range]
            self.ax.plot(self.T_db_range, w_values, 'k-', linewidth=0.5)
            x_pos = self.T_db_range[0] - 1
            y_pos = w_values[0]
            self.ax.text(x_pos, y_pos, f'{h_value} kJ/kg', va='center', ha='left', color='black', fontsize=8)

        self.ax.set_ylim(0, self.max_w_value)
        self.ax.set_title(self.title)
        self.ax.set_xlabel('Température de bulbe sec (°C)')
        self.ax.set_ylabel('Humidité spécifique (g/kg air sec)')
        self.ax.yaxis.set_label_position("right")
        self.ax.yaxis.tick_right()
        self.ax.grid(True)

    #func_w (RH, P, P_sat)  
    def add_points(self, points):
        for point in points:
            T_db, w = None, None
            if 'T_db' in point and 'RH' in point:
                T_db, w = point['T_db'], air_humide.func_w(RH=point['RH'], T_db=point['T_db'])
            elif 'h' in point and 'T_db' in point:
                T_db, w = point['T_db'], air_humide.func_w(h=point['h'], T_db=point['T_db'])
            elif 'w' in point and 'T_db' in point:
                T_db, w = point['T_db'], point['w']
            elif 'RH' in point and 'w' in point:
                T_db, w = air_humide.func_T_db(RH=point['RH'], w=point['w']),point['w']
            elif 'h' in point and 'w' in point:
                T_db, w = air_humide.func_T_db(h=point['h'], w=point['w']),point['w']
            if T_db is not None and w is not None:
                self.ax.plot(T_db, w, 'ro')

    def show(self):
        plt.show()