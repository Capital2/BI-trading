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
import { parse } from "stylis";

function Config({ days: propsDays, initialBalance: propsInitialBalance, predict }) {
    const [days, setDays] = useState(propsDays)
    const [initialBalance, setInitialBalance] = useState(propsInitialBalance)

    const handleSubmit = (e) => {
        e.preventDefault();
        predict(days, initialBalance)
    }

    return (
        <Card style={{ padding: "12px", marginBottom: "50px" }}>
            <SoftBox pt={2} px={2} mb={2}>
                <SoftTypography variant="h6" fontWeight="medium" textTransform="capitalize">
                    Forecast Configuration
                </SoftTypography>
            </SoftBox>
            <SoftBox component="form" role="form" onSubmit={handleSubmit}>
                <SoftBox mb={2}>
                    <SoftBox mb={1} ml={0.5}>
                        <SoftTypography component="label" variant="caption" fontWeight="bold">
                            Days in the future
                        </SoftTypography>
                    </SoftBox>
                    <SoftInput
                        id="days"
                        name="days"
                        onChange={(e) => setDays(e.target.value)}
                        type="text"
                        placeholder="100"
                        value={days}
                    />
                </SoftBox>
                <SoftBox mb={2}>
                    <SoftBox mb={1} ml={0.5}>
                        <SoftTypography component="label" variant="caption" fontWeight="bold">
                            Starting amount
                        </SoftTypography>
                    </SoftBox>
                    <SoftInput
                        id="amount"
                        name="amount"
                        onChange={(e) => setInitialBalance(e.target.value)}
                        type="text"
                        placeholder="Amount"
                        value={initialBalance}
                    />
                </SoftBox>
                <SoftBox mt={1} component="div" style={{ textAlign: "center" }}>
                    <SoftButton variant="gradient" color="info" type="submit">
                        Confirm
                    </SoftButton>
                </SoftBox>
            </SoftBox>
        </Card>
    );
}

export default Config;
