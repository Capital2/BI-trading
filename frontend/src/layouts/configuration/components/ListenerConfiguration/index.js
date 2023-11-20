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
// Soft UI Dashboard React components

import { Link } from "react-router-dom";

import SoftInput from "components/SoftInput";
import SoftButton from "components/SoftButton";
import SoftAlert from "components/SoftAlert";
// @mui material components
import Icon from "@mui/material/Icon";
import axios from "axios";
import Swal from "sweetalert2";

function ListenerConfiguration() {
  const [currentListenerState, setCurrentListenerState] = useState(false);

  const getListenerState = () => {
    axios
      .get("http://localhost:8000/sensor/get/listener_state")
      .then((response) => {
        setCurrentListenerState(response.data.state);
      })
      .catch((error) => {
        console.log("The server error for listener state");
        console.log(error);
      });
  };

  const setListenerState = (reqBody) => {
    axios
      .put("http://localhost:8000/sensor/configure_listener", reqBody)
      .then((response) => {
        Swal.fire({
          icon: "success",
          title: "Listener Configuration",
          text: currentListenerState
            ? "Data collection is enabled succesffuly"
            : "Data collection is disabled succesffuly",
        });
      })
      .catch((error) => {
        console.log("The server error");
        console.log(error);
        Swal.fire({
          icon: "error",
          title: "Listener Configuration",
          text: "Error in the listener configuration process",
        });
      });
  };

  const handleListenerConfiguration = (e) => {
    setCurrentListenerState(e.target.checked);
  };

  const handleSubmitListenerConfiguration = (e) => {
    e.preventDefault();
    setListenerState({ collect: currentListenerState });
  };

  useEffect(() => {
    getListenerState();
  }, []);

  return (
    <Card style={{ padding: "12px", height: "500px" }}>
      <SoftBox pt={2} px={2} mb={2}>
        <SoftTypography variant="h6" fontWeight="medium" textTransform="capitalize">
          Listener Configurqtion
        </SoftTypography>
      </SoftBox>
      <SoftAlert color="dark" mt={3}>
        To enable data collection set the check box to active state
      </SoftAlert>
      <SoftAlert color="dark" mt={1}>
        To disable the data collection set the check box to the enactive state
      </SoftAlert>
      <SoftBox component="form" role="form" onSubmit={handleSubmitListenerConfiguration}>
        <SoftBox display="flex" py={1} mb={0.25}>
          <SoftBox mt={0.25}>
            <Switch
              id="currentListenerState"
              name="currentListenerState"
              checked={currentListenerState}
              onChange={handleListenerConfiguration}
            />
          </SoftBox>
          <SoftBox width="80%" ml={2}>
            <SoftTypography variant="button" fontWeight="regular" color="text">
              Listener State
            </SoftTypography>
          </SoftBox>
        </SoftBox>
        <SoftBox mt={9} mb={1} component="div" style={{ textAlign: "center" }}>
          <SoftButton variant="gradient" color="warning" type="submit">
            Configure
          </SoftButton>
        </SoftBox>
      </SoftBox>
    </Card>
  );
}

export default ListenerConfiguration;
