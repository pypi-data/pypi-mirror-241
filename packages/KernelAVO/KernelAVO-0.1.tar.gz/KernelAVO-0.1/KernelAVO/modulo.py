import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class Kernel:
    def __init__(self,data,sigma):
        self.sigma=sigma
        self.data=data

    def gaussian(self):
        nuevos_casos=self.data['NUEVOS_CASOS']
        smoothed_data = np.zeros_like(nuevos_casos)
        n = len(nuevos_casos)

        for i in range(n):
            weights=np.exp(-((np.arange(n) - i) ** 2) / (2 * self.sigma ** 2)) / (np.sqrt(2 * np.pi) * self.sigma)
            smoothed_data[i] = np.sum(nuevos_casos * weights) / np.sum(weights)

        return smoothed_data

    def tricube(self):
        nuevos_casos=self.data['NUEVOS_CASOS']
        smoothed_data = np.zeros_like(nuevos_casos)
        n = len(nuevos_casos)

        for i in range(len(nuevos_casos)):
            weights = np.where(np.abs(((np.arange(len(nuevos_casos))-i)/self.sigma)) <= 1, (1-np.abs(((np.arange(len(nuevos_casos))-i)/self.sigma))**3)**3, 0)
            weights /= np.sum(weights)  
            smoothed_data[i] = np.sum(weights * nuevos_casos)
    
        return smoothed_data

    def epanechnikov(self):
        nuevos_casos=self.data['NUEVOS_CASOS']
        smoothed_data = np.zeros_like(nuevos_casos)
        n = len(nuevos_casos)

        for i in range(len(nuevos_casos)):
            weights = np.where(np.abs(((np.arange(len(nuevos_casos)) - i)/self.sigma)) <= 1, 3/4 * (1-((np.arange(len(nuevos_casos))-i)/self.sigma)**2), 0)
            weights /= np.sum(weights)  
            smoothed_data[i] = np.sum(weights * nuevos_casos)
    
        return smoothed_data                
        
    def plotgaussian(self):
        fecha_actualizacion = self.data['FECHA_ACTUALIZACION']
        fecha_actualizacion=np.array([fecha_actualizacion[i][0:10] for i in range(len(fecha_actualizacion))])
        nuevos_casos=self.data['NUEVOS_CASOS']
        smoothed_nuevos_casos=self.gaussian()

        n = len(fecha_actualizacion)
        show_every_n = 50  
        indices = np.arange(0, n, show_every_n)
        show_dates = fecha_actualizacion[indices]

        plt.figure(figsize=(10, 6))
        plt.plot(fecha_actualizacion, nuevos_casos,label="Datos",markersize=5, marker='o', linestyle='', color='b',alpha=0.5)
        plt.plot(fecha_actualizacion, smoothed_nuevos_casos, label="Gaussian", color='r', linewidth=2)
        plt.legend()
        plt.title('Casos nuevos de COVID-19')
        plt.xlabel('Fecha de actualización')
        plt.ylabel('Número de nuevos casos')
        plt.xticks(rotation=45)
        plt.xticks(indices, show_dates, fontsize=8)
        plt.tight_layout()
        plt.show()

    def plottricube(self):
        fecha_actualizacion = self.data['FECHA_ACTUALIZACION']
        fecha_actualizacion=np.array([fecha_actualizacion[i][0:10] for i in range(len(fecha_actualizacion))])
        nuevos_casos=self.data['NUEVOS_CASOS']
        smoothed_nuevos_casos=self.tricube()

        n = len(fecha_actualizacion)
        show_every_n = 50  
        indices = np.arange(0, n, show_every_n)
        show_dates = fecha_actualizacion[indices]

        plt.figure(figsize=(10, 6))
        plt.plot(fecha_actualizacion, nuevos_casos,label="Datos",markersize=5, marker='o', linestyle='', color='b',alpha=0.5)
        plt.plot(fecha_actualizacion, smoothed_nuevos_casos, label="Tricube", color='r', linewidth=2)
        plt.legend()
        plt.title('Casos nuevos de COVID-19')
        plt.xlabel('Fecha de actualización')
        plt.ylabel('Número de nuevos casos')
        plt.xticks(rotation=45)
        plt.xticks(indices, show_dates, fontsize=8)
        plt.tight_layout()
        plt.show()

    def plotepanechnikov(self):
        fecha_actualizacion = self.data['FECHA_ACTUALIZACION']
        fecha_actualizacion=np.array([fecha_actualizacion[i][0:10] for i in range(len(fecha_actualizacion))])
        nuevos_casos=self.data['NUEVOS_CASOS']
        smoothed_nuevos_casos=self.epanechnikov()

        n = len(fecha_actualizacion)
        show_every_n = 50  
        indices = np.arange(0, n, show_every_n)
        show_dates = fecha_actualizacion[indices]

        plt.figure(figsize=(10, 6))
        plt.plot(fecha_actualizacion, nuevos_casos,label="Datos",markersize=5, marker='o', linestyle='', color='b',alpha=0.5)
        plt.plot(fecha_actualizacion, smoothed_nuevos_casos, label="Tricube", color='r', linewidth=2)
        plt.legend()
        plt.title('Casos nuevos de COVID-19')
        plt.xlabel('Fecha de actualización')
        plt.ylabel('Número de nuevos casos')
        plt.xticks(rotation=45)
        plt.xticks(indices, show_dates, fontsize=8)
        plt.tight_layout()
        plt.show()

    def plotcomparation(self):
        fecha_actualizacion = self.data['FECHA_ACTUALIZACION']
        fecha_actualizacion=np.array([fecha_actualizacion[i][0:10] for i in range(len(fecha_actualizacion))])
        nuevos_casos=self.data['NUEVOS_CASOS']
        smoothed_nuevos_casos=self.gaussian()
        smoothed_nuevos_casos2=self.tricube()
        smoothed_nuevos_casos3=self.epanechnikov()

        n = len(fecha_actualizacion)
        show_every_n = 50  
        indices = np.arange(0, n, show_every_n)
        show_dates = fecha_actualizacion[indices]

        plt.figure(figsize=(10, 6))
        plt.plot(fecha_actualizacion, smoothed_nuevos_casos, label="Gaussian", color='r', linewidth=2)
        plt.plot(fecha_actualizacion, smoothed_nuevos_casos2, label="Tricube", color='g', linewidth=2)
        plt.plot(fecha_actualizacion, smoothed_nuevos_casos3, label="Epanechnikov", color='cyan', linewidth=2)
        plt.legend()
        plt.title(f"Comparación para parámetro de suavizado $\sigma={self.sigma}$")
        plt.xlabel('Fecha de actualización')
        plt.ylabel('Número de nuevos casos')
        plt.xticks(rotation=45)
        plt.xticks(indices, show_dates, fontsize=8)
        plt.tight_layout()
        plt.show()
