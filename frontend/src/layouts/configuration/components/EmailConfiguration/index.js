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
import Swal from "sweetalert2";

import { Link } from "react-router-dom";

import SoftInput from "components/SoftInput";
import SoftButton from "components/SoftButton";
import axios from "axios";
import NotificationItem from "examples/Items/NotificationItem";

function SensorConfiguration() {
  const [userEmail, setUserEmail] = useState("");
  const [emailResetFlags, setEmailResetFlags] = useState({
    hum_email_sent: false,
    temp_email_sent: false,
  });

  const getEmail = () => {
    axios
      .get("http://localhost:8000/sensor/get/receiver")
      .then((response) => {
        // console.log("The server response");
        // console.log(response);

        if (response.data.email !== null) {
          setUserEmail(response.data.email);
        }
      })
      .catch((error) => {
        console.log("The server error");
        console.log(error);
      });
  };

  const setEmail = (reqBody) => {
    axios
      .post("http://localhost:8000/sensor/set/receiver", reqBody)
      .then((response) => {
        // console.log("The server response");
        // console.log(response);
        Swal.fire({
          icon: "success",
          title: "Email Configuration",
          text: "You email is set successfully",
        });
      })
      .catch((error) => {
        console.log("The server error");
        console.log(error);
      });
  };

  const handleUserEmailChange = (e) => {
    setUserEmail(e.target.value);
  };

  const handleSubmitUserEmail = (e) => {
    e.preventDefault();
    // console.log("submit data to the back end");
    setEmail({ email: userEmail });
  };

  const manageEmailResetFlags = (e) => {
    // console.log(e.target.id);
    // console.log(e.target.checked);
    setEmailResetFlags({ ...emailResetFlags, [e.target.id]: e.target.checked });
  };

  const resetEmailFlags = (reqBody) => {
    axios
      .put("http://localhost:8000/sensor/reset_email_notifications_flags", reqBody)
      .then((response) => {
        // console.log("The server response");
        // console.log(response);
        Swal.fire({
            icon: "success",
            title: "Flags Reset",
            text: "Email falgs are reset successfully",
          });
      })
      .catch((error) => {
        console.log("The server error");
        console.log(error);
      });
  };

  const handleSubmitEmailResetFlags = (e) => {
    e.preventDefault();
    resetEmailFlags(emailResetFlags);
  };

  useEffect(() => {
    // console.log("comp mount");
    getEmail();
  }, []);

  return (
    <Card style={{ padding: "12px", height: "500px" }}>
      <SoftBox pt={2} px={2} mb={2}>
        <SoftTypography variant="h6" fontWeight="medium" textTransform="capitalize">
          Email Configurqtion
        </SoftTypography>
      </SoftBox>
      <SoftBox component="form" role="form" onSubmit={handleSubmitUserEmail}>
        <SoftBox mb={2}>
          <SoftBox mb={1} ml={0.5}>
            <SoftTypography component="label" variant="caption" fontWeight="bold">
              Email used in urgence cases
            </SoftTypography>
          </SoftBox>
          <SoftInput
            id="userEmail"
            name="userEmail"
            onChange={handleUserEmailChange}
            type="email"
            placeholder="user@domain.com"
            value={userEmail}
          />
        </SoftBox>
        <SoftBox mt={4} mb={1} component="div" style={{ textAlign: "center" }}>
          <SoftButton variant="gradient" color="info" type="submit">
            Confirm
          </SoftButton>
        </SoftBox>
      </SoftBox>

      <SoftBox component="form" role="form" mt={3} onSubmit={handleSubmitEmailResetFlags}>
        <SoftBox mb={1} ml={0.5}>
          <SoftTypography component="label" variant="caption" fontWeight="bold">
            Reset email sending flags
          </SoftTypography>
        </SoftBox>
        <SoftBox display="flex" py={1} mb={0.25}>
          <SoftBox mt={0.25}>
            <Switch
              id="temp_email_sent"
              name="temp_email_sent"
              checked={emailResetFlags.temp_email_sent}
              onChange={manageEmailResetFlags}
            />
          </SoftBox>
          <SoftBox width="80%" ml={2}>
            <SoftTypography variant="button" fontWeight="regular" color="text">
              Temrature sending flags
            </SoftTypography>
          </SoftBox>
        </SoftBox>
        <SoftBox display="flex" py={1} mb={0.25}>
          <SoftBox mt={0.25}>
            <Switch
              id="hum_email_sent"
              name="hum_email_sent"
              checked={emailResetFlags.hum_email_sent}
              onChange={manageEmailResetFlags}
            />
          </SoftBox>
          <SoftBox width="80%" ml={2}>
            <SoftTypography variant="button" fontWeight="regular" color="text">
              Humidity sending flags
            </SoftTypography>
          </SoftBox>
        </SoftBox>
        <SoftBox mt={4} mb={1} component="div" style={{ textAlign: "center" }}>
          <SoftButton variant="gradient" color="info" type="submit">
            Reset
          </SoftButton>
        </SoftBox>
      </SoftBox>
    </Card>
  );
}

export default SensorConfiguration;
