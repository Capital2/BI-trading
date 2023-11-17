/**
=========================================================
* Soft UI Dashboard React - v4.0.0
=========================================================

* Product Page: https://www.creative-tim.com/product/soft-ui-dashboard-react
* Copyright 2022 Creative Tim (https://www.creative-tim.com)

Coded by www.creative-tim.com

 =========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
*/
import React, { useState, useEffect } from 'react';

function GradientLineChartData() {
  const [humidityValues, setHumidityValues] = useState([]);
  const [temperatureValues, setTemperatureValues] = useState([]);
  const [labels, setLabels] = useState([]); // same labels for both humidity and temperature

  useEffect(() => {
      fetch('http://127.0.0.1:8000/humidity/all')
        .then(response => response.json())
        .then(data => {
          let newHumidityValues = [], newLabels = [];
          data.map((item) => {
            newHumidityValues.push(item.value);
            const formattedTime = new Date(item.created_at).toLocaleTimeString('en-US', { hour: 'numeric', minute: 'numeric', hour12: true });
            newLabels.push(formattedTime);
          });
          setHumidityValues(newHumidityValues);
          setLabels(newLabels);
        });

      fetch('http://127.0.0.1:8000/temperature/all')
        .then(response => response.json())
        .then(data => {
          let newTemperatureValues = [];
          data.map((item) => {
            newTemperatureValues.push(item.value);
          });
          setTemperatureValues(newTemperatureValues);
        });
  }, []);
  

  const chart = {
    labels: labels,
    datasets: [
      {
        label: "Temperature",
        color: "info",
        data: temperatureValues,
      },
      {
        label: "Humidity",
        color: "dark",
        data: humidityValues,
      },
    ],
  }
  return chart;
};

export default GradientLineChartData;
