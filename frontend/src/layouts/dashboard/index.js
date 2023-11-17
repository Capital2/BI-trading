// @mui material components
import Grid from "@mui/material/Grid";

// Soft UI Dashboard React components
import SoftBox from "components/SoftBox";

// Soft UI Dashboard React examples
import DashboardLayout from "examples/LayoutContainers/DashboardLayout";
import Footer from "examples/Footer";

// Dashboard layout components
import Projects from "layouts/dashboard/components/Projects";

// Data
import ReportsBarChartData from "layouts/dashboard/data/reportsBarChartData";
import { useEffect, useState } from "react";
import Config from './components/Config'
import Card from "@mui/material/Card";
import SoftTypography from "components/SoftTypography";

// Charts
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';
import { Line } from 'react-chartjs-2';

import Header from './components/Header'

function Dashboard() {
  const [CurrentSelectedTab, setCurrentSelectedTab] = useState(0)
  const [days, setDays] = useState(20)
  const [initialBalance, setInitialBalance] = useState(5000)
  const [dashboardData, setDashboardData] = useState(null)
  const [acco, setAcco] = useState(null)
  const [fisb, setFisb] = useState(null)
  const [atnfw, setAtnfw] = useState(null)
  const [gme, setGme] = useState(null)
  const [ascbr, setAscbr] = useState(null)
  const [data, setData] = useState(null)
  const [isLoading, setIsLoading] = useState(true)


  const fetchPredictionData = async (days, initialBalance) => {
    fetch(`http://20.111.23.22:32771/prediction/market_activity_forecast/${days}/${initialBalance}/ACCO`)
      .then(response => response.json())
      .then(data => setAcco(data));

    fetch(`http://20.111.23.22:32771/prediction/market_activity_forecast/${days}/${initialBalance}/FISB`)
      .then(response => response.json())
      .then(data => setFisb(data));

    fetch(`http://20.111.23.22:32771/prediction/market_activity_forecast/${days}/${initialBalance}/ATNFW`)
      .then(response => response.json())
      .then(data => setAtnfw(data));

    fetch(`http://20.111.23.22:32771/prediction/market_activity_forecast/${days}/${initialBalance}/GME`)
      .then(response => response.json())
      .then(data => setGme(data));

    fetch(`http://20.111.23.22:32771/prediction/market_activity_forecast/${days}/${initialBalance}/ASCBR`)
      .then(response => response.json())
      .then(data => setAscbr(data));

  }

  const fetchDashboardData = () => {
    fetch('http://20.111.23.22:32771/oplap/cube_details')
      .then(response => response.json())
      .then(data => setData(data));
  }

  // Prediction widget
  const predictionOptions = {
    responsive: true,
    plugins: {
      legend: {
        position: 'top',
      },
      title: {
        display: true,
        text: 'Agents Performance Monitoring',
      },
    },
  };

  const getLabels = () => {
    let res = []
    for (let i = 1; i <= days; i++) {
      res.push(i)
    }

    return res
  }
  // Generate the labels
  const predictionLabels = getLabels();

  // Predictions data
  const predictionData = {
    labels: predictionLabels,
    datasets: [
      {
        label: 'ACCO',
        data: acco !== null ? acco['prediction'] : [],
        borderColor: 'rgb(255, 99, 132)',
        backgroundColor: 'rgba(255, 99, 132, 0.5)',
      },
      {
        label: 'FISB',
        data: fisb !== null ? fisb['prediction'] : [],
        borderColor: 'rgb(53, 162, 235)',
        backgroundColor: 'rgba(53, 162, 235, 0.5)',
      },
      {
        label: 'ATNFW',
        data: atnfw !== null ? atnfw['prediction'] : [],
        borderColor: 'rgb(53, 320, 235)',
        backgroundColor: 'rgba(53, 162, 235, 0.7)',
      },
      {
        label: 'GME',
        data: gme !== null ? gme['prediction'] : [],
        borderColor: 'rgb(70, 100, 235)',
        backgroundColor: 'rgba(70, 100, 235, 0.7)',
      },
      {
        label: 'ASCBR',
        data: ascbr !== null ? ascbr['prediction'] : [],
        borderColor: 'rgb(90, 50, 35)',
        backgroundColor: 'rgba(90, 50, 30, 0.7)',
      },
    ]
  };

  const predict = async (days, initialBalance) => {

    setAcco(null)
    setFisb(null)
    setAtnfw(null)
    setGme(null)
    setAscbr(null)


    setDays(days)
    setInitialBalance(initialBalance)
    setIsLoading(true)

    await fetchPredictionData(days, initialBalance)
  }

  useEffect(() => {
    fetchPredictionData(days, initialBalance);
    fetchDashboardData();
  }, []);

  useEffect(() => {
    if (acco && fisb && atnfw && gme && ascbr) {
      setIsLoading(false)
    }
  }, [acco, fisb, atnfw, gme, ascbr])


  const renderWidget = (obj) => {
    let jsx = []
    for (let key in obj) {
      jsx.push(<p>{key}: {obj[key]}</p>)
    }

    return jsx
  }
  return (
    <DashboardLayout>
      <Header setCurrentSelectedTab={setCurrentSelectedTab} />
      <SoftBox py={3}>
        <Grid container spacing={3} mb={6}>
          <Grid item xs={6} md={4} lg={3}>
            <Card>
              <SoftBox display="flex" justifyContent="space-between" alignItems="center" p={3}>
                <div style={{ height: '235px' }}>
                  <SoftBox>
                    <SoftTypography variant="h6" gutterBottom>
                      Max Share
                    </SoftTypography>
                    <hr />
                    <div style={{ padding: '8px', marginTop: '20px' }}>
                      {(data !== null && data['Max_Close'] !== null) ? (renderWidget(data['Max_Close'])) : (<center><div className="loader"></div></center>)}
                    </div>
                  </SoftBox>
                </div>
              </SoftBox>
            </Card>
          </Grid>
          <Grid item xs={6} md={4} lg={3}>
            <Card>
              <SoftBox display="flex" justifyContent="space-between" alignItems="center" p={3}>
                <div style={{ height: '235px' }}>
                  <SoftBox>
                    <SoftTypography variant="h6" gutterBottom>
                      Min Share
                    </SoftTypography>
                    <hr />
                    <div style={{ padding: '8px', marginTop: '20px' }}>
                      {(data !== null && data['Min_Close'] !== null) ? (renderWidget(data['Min_Close'])) : (<center><div className="loader"></div></center>)}
                    </div>
                  </SoftBox>
                </div>
              </SoftBox>
            </Card>
          </Grid>
          <Grid item xs={6} md={4} lg={3}>
            <Card>
              <SoftBox display="flex" justifyContent="space-between" alignItems="center" p={3}>
                <div style={{ height: '235px' }}>
                  <SoftBox>
                    <SoftTypography variant="h6" gutterBottom>
                      Makret Activity
                    </SoftTypography>
                    <hr />
                    <div style={{ padding: '8px', marginTop: '20px' }}>                      
                      {(data !== null && data['Market_Activity'] !== null) ? (<p>Total Number: {data && data['Market_Activity']}</p>) : (<center><div className="loader"></div></center>)}
                    </div>
                  </SoftBox>
                </div>
              </SoftBox>
            </Card>
          </Grid>
          <Grid item xs={6} md={4} lg={3}>
            <Card>
              <SoftBox display="flex" justifyContent="space-between" alignItems="center" p={3}>
                <div style={{ height: '235px' }}>
                  <SoftBox>
                    <SoftTypography variant="h6" gutterBottom>
                      Mean Volume Per Share
                    </SoftTypography>
                    <hr />
                    <div style={{ padding: '8px', marginTop: '20px' }}>
                      {(data !== null && data['Mean_Volume'] !== null) ? (renderWidget(data['Mean_Volume'])) : (<center><div className="loader"></div></center>)}
                    </div>
                  </SoftBox>
                </div>
              </SoftBox>
            </Card>
          </Grid>
        </Grid>
        <SoftBox mb={8}>
          <Grid container spacing={3}>
            <Grid item xs={12} lg={12}>
              <Config initialBalance={initialBalance} days={days} predict={predict} />
            </Grid>
            <Grid item xs={12} lg={12}>
              {!isLoading ? (
                <Line options={predictionOptions} data={predictionData} />
              ) : (<center><div class="loader"></div></center>)}

            </Grid>
          </Grid>
        </SoftBox>

      </SoftBox>
      <Footer />
    </DashboardLayout>
  );
}

export default Dashboard;
