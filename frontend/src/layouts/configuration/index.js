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

// @mui material components
import Grid from "@mui/material/Grid";
import Card from "@mui/material/Card";

// Soft UI Dashboard React components
import SoftBox from "components/SoftBox";
import SoftTypography from "components/SoftTypography";

// Soft UI Dashboard React examples
import DashboardLayout from "examples/LayoutContainers/DashboardLayout";
import Footer from "examples/Footer";


// Overview page components
import Header from "layouts/configuration/components/Header";
import SensorConfiguration from "layouts/configuration/components/SensorConfiguration";
import EmailConfiguration from "layouts/configuration/components/EmailConfiguration";
import ListenerConfiguration from "layouts/configuration/components/ListenerConfiguration";


import { useState } from "react";

function Overview() {
  const [currentSelectedTab, setCurrentSelectedTab] = useState(0);

  return (
    <DashboardLayout>
      <Header setCurrentSelectedTab={setCurrentSelectedTab} />
      <SoftBox mt={5} mb={2}>
        <Card>
          <SoftBox pt={2} px={2}>
            <SoftBox mb={0.5}>
              <SoftTypography variant="h6" fontWeight="medium">
                Description
              </SoftTypography>
            </SoftBox>
            <SoftBox mb={1}>
              <SoftTypography variant="button" fontWeight="regular" color="text">
                {currentSelectedTab === 0 && (
                  <p>
                    The sensor confifuration panel will allow to mange your ESP32 configuration, by
                    creating, updating, visualizing and deleting your configuration
                  </p>
                )}

                {currentSelectedTab === 1 && (
                  <p>
                    Listener configuration panel will allow you to configure your data collection
                    system.
                    <br /> When creating a sensor configuration the system will launch a listener
                    that is going to listn for the data gathered from the ESP32. By default the
                    system will not write the data to the database until you configure it. <br />
                    The goal is to have an optimized storage system that easy to manage. <br />
                    Also our listener will notiy you by email if threshold is hit so you can react
                    any urgence case
                  </p>
                )}

                {currentSelectedTab === 2 && <p>Our system requires that you provide an email that is going to be used in case of urgence cases <br />
                When you receive an email froml our application you must reset the flags to be notified in the upcoming urgence case</p>}
              </SoftTypography>
            </SoftBox>
          </SoftBox>
        </Card>
      </SoftBox>
      <SoftBox mt={5} mb={3}>
        <Grid container spacing={3}>
          <Grid item xs={12} md={6} xl={4}>
            <EmailConfiguration />
          </Grid>
          <Grid item xs={12} xl={4}>
            <SensorConfiguration  />
          </Grid>
          <Grid item xs={12} xl={4}>
            <ListenerConfiguration  />
          </Grid>       
        </Grid>
      </SoftBox>

      <Footer />
    </DashboardLayout>
  );
}

export default Overview;
