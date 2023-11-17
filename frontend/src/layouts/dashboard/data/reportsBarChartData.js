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
import React, { useState, useEffect } from "react";

function ReportsBarChartData() {
  const [humidityMaxValues, setHumidityMaxValues] = useState([]);
  const [humidityMinValues, setHumidityMinValues] = useState([]);
  const [temperatureMaxValues, setTemperatureMaxValues] = useState([]);
  const [temperatureMinValues, setTemperatureMinValues] = useState([]);
  const [labels, setLabels] = useState([]); // same labels for both humidity and temperature

  useEffect(() => {
    fetch("http://127.0.0.1:8000/humidity/get-daily-min-max-humidities")
      .then((response) => response.json())
      .then((data) => {
        let newHumidityMaxValues = [];
        let newHumidityMinValues = [];
        let newLabels = [];
        data.map((item) => {
          newHumidityMaxValues.push(item.max_temp);
          newHumidityMinValues.push(item.min_temp);
          newLabels.push(item.hour);
        });
        setHumidityMaxValues(newHumidityMaxValues);
        setHumidityMinValues(newHumidityMinValues);
        setLabels(newLabels);
      });

    fetch("http://127.0.0.1:8000/temperature/get-daily-min-max-temperatures")
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        let newTemperatureMaxValues = [];
        let newTemperatureMinValues = [];
        data.map((item) => {
          newTemperatureMaxValues.push(item.max_temp);
          newTemperatureMinValues.push(item.min_temp);
        });
        setTemperatureMaxValues(newTemperatureMaxValues);
        setTemperatureMinValues(newTemperatureMinValues);
      });
  }, []);

  const maxTemperature = Math.max(...temperatureMaxValues);
  const maxTemperaturePercentage = (maxTemperature / 50) * 100;
  const maxHumidity = Math.max(...humidityMaxValues);
  const maxHumidityPercentage = (maxHumidity / 100) * 100;
  const minTemperature = Math.min(...temperatureMinValues);
  const minTemperaturePercentage = (minTemperature / 50) * 100;
  const minHumidity = Math.min(...humidityMinValues);
  const minHumidityPercentage = (minHumidity / 100) * 100;

  const tempColor = (value) => {
    if (value > 40) {
      return "error";
    } else if (value > 30) {
      return "warning";
    } else {
      return "info";
    }
  };

  const humidityColor = (value) => {
    if (value > 80) {
      return "error";
    } else if (value > 60) {
      return "warning";
    } else {
      return "info";
    }
  };

  const reportsBarChartData = {
    chart: {
      labels: labels,
      datasets: [
        {
          chartType: "thin-bar",
          label: "Max",
          data: temperatureMaxValues,
          color: "error",
        },
        {
          chartType: "thin-bar",
          label: "Min",
          data: temperatureMinValues,
          color: "info",
        },
      ],
    },
    items: [
      {
        icon: { color: tempColor(maxTemperature), component: "" },
        label: "Max Temp",
        progress: { content: maxTemperature + "°C", percentage: maxTemperaturePercentage },
      },
      {
        icon: { color: tempColor(minTemperature), component: "" },
        label: "Min Temp",
        progress: { content: minTemperature + "°C", percentage: minTemperaturePercentage },
      },
      {
        icon: { color: humidityColor(maxHumidity), component: "" },
        label: "Max Hum",
        progress: { content: maxHumidity + "%", percentage: maxHumidityPercentage },
      },
      {
        icon: { color: humidityColor(minHumidity), component: "" },
        label: "Min Hum",
        progress: { content: minHumidity + "%", percentage: minHumidityPercentage },
      },
    ],
  };

  return reportsBarChartData;
}

export default ReportsBarChartData;
