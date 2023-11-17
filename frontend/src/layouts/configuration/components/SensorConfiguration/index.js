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

import { useState, useEffect } from "react";

// @mui material components
import Card from "@mui/material/Card";
import Switch from "@mui/material/Switch";

// Soft UI Dashboard React components
import SoftBox from "components/SoftBox";
import SoftTypography from "components/SoftTypography";

import SoftInput from "components/SoftInput";
import SoftButton from "components/SoftButton";
import axios from "axios";
import Swal from "sweetalert2";

function SensorConfiguration() {
  const [sensorConfig, setSensorConfig] = useState({});
  const [mutation, setMutation] = useState(false);

  const getSensorConfiguration = () => {
    axios
      .get("http://localhost:8000/sensor/config/get/1")
      .then((response) => {
        console.log("response for get sensor config");
        console.log(response.data);
        setSensorConfig(response.data);
        setMutation(true);
      })
      .catch((error) => {
        console.log("The server error for getting the sensor config");
        console.log(error);
        setSensorConfig({});
        setMutation(false);
      });
  };

  const createSensorConfiguration = (reqBody) => {
    axios
      .post("http://localhost:8000/sensor/configure", reqBody)
      .then((response) => {
        console.log("the sensor creaton server response");
        console.log(response.data);
        setSensorConfig(response.data);
        Swal.fire({
          icon: "success",
          title: "Sensor Configuration",
          text: "The sensor is configured successfully",
        });
      })
      .catch((error) => {
        console.log("The server error for create sensor config");
        console.log(error);
        Swal.fire({
          icon: "error",
          title: "Sensor Configuration",
          text: "Error in the sensor configuration",
        });
      });
  };

  const updateSensorConfiguration = (reqBody) => {
    axios
      .put("http://localhost:8000/sensor/configure/1", reqBody)
      .then((response) => {
        console.log("the sensor update server response");
        console.log(response.data);
        Swal.fire({
          icon: "success",
          title: "Sensor Configuration",
          text: "The sensor configuration is updated successfully",
        });
      })
      .catch((error) => {
        console.log("The server error for update sensor config");
        console.log(error);
        Swal.fire({
          icon: "error",
          title: "Sensor Configuration",
          text: "Error occured while updating the sensor configuration",
        });
      });
  };

  const deleteSensorConfiguration = () => {
    axios
      .delete("http://localhost:8000/sensor/delete_config/1")
      .then((response) => {
        console.log("the sensor delete server response");
        console.log(response.data);
        Swal.fire({
          icon: "success",
          title: "Sensor Configuration",
          text: "The sensor configuration is deleted successfully"            
        });
      })
      .catch((error) => {
        console.log("The server error for delete sensor config");
        console.log(error);
        Swal.fire({
          icon: "error",
          title: "Sensor Configuration",
          text: "Error occured while deleting the sensor configuration. that can due to that the configuration dosen't exist.",
        });
      });
  };

  const handleListenerConfigMutation = (e) => {
    e.preventDefault();
    if (!mutation) {
      // console.log("data to sent to the backend");
      // console.log(sensorConfig);
      createSensorConfiguration({
        temperature: parseInt(sensorConfig.temperature),
        humidity: parseInt(sensorConfig.humidity),
        purpose: sensorConfig.purpose,
      });
    } else {
      let tmp = {
        ...sensorConfig,
        temperature: parseInt(sensorConfig.temperature),
        humidity: parseInt(sensorConfig.humidity),
      };

      delete tmp.id;
      updateSensorConfiguration(tmp);
    }
  };

  const handleSensorConfig = (e) => {
    setSensorConfig({
      ...sensorConfig,
      [e.target.id]: e.target.value,
    });
  };

  useEffect(() => {
    getSensorConfiguration();
  }, []);

  return (
    <Card style={{ padding: "12px", height: "500px" }}>
      <SoftBox pt={2} px={2} mb={2}>
        <SoftTypography variant="h6" fontWeight="medium" textTransform="capitalize">
          Sensor Configuration
        </SoftTypography>
      </SoftBox>

      <SoftBox component="form" role="form" onSubmit={handleListenerConfigMutation}>
        <SoftBox mb={2}>
          <SoftBox mb={1} ml={0.5}>
            <SoftTypography component="label" variant="caption" fontWeight="bold">
              Temperature
            </SoftTypography>
          </SoftBox>
          <SoftInput
            id="temperature"
            name="temperature"
            type="text"
            placeholder="Write an integer value"
            onChange={handleSensorConfig}
          />
        </SoftBox>
        <SoftBox mb={2}>
          <SoftBox mb={1} ml={0.5}>
            <SoftTypography component="label" variant="caption" fontWeight="bold">
              Humidity
            </SoftTypography>
          </SoftBox>
          <SoftInput
            id="humidity"
            name="humidity"
            type="text"
            placeholder="Write an integer value"
            onChange={handleSensorConfig}
          />
        </SoftBox>
        <SoftBox mb={2}>
          <SoftBox mb={1} ml={0.5}>
            <SoftTypography component="label" variant="caption" fontWeight="bold">
              Purpose
            </SoftTypography>
          </SoftBox>
          <SoftInput
            id="purpose"
            name="purpose"
            type="Text"
            placeholder="Reason behind this configuration"
            onChange={handleSensorConfig}
          />
        </SoftBox>
        <SoftBox mt={11} mb={1} component="div" style={{ textAlign: "center" }}>
          <SoftButton
            type="submit"
            variant="gradient"
            color="success"
            style={{ marginRight: "10px" }}
          >
            Mutate
          </SoftButton>
          <SoftButton
            type="button"
            variant="gradient"
            color="error"
            onClick={deleteSensorConfiguration}
          >
            Delete
          </SoftButton>
        </SoftBox>
      </SoftBox>
    </Card>
  );
}

export default SensorConfiguration;
