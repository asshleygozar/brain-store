'use client';
import { useState } from 'react';
import LandingPage from './(landing-page)/LandingPage';
import Dashboard from './(dashboard)/Dashboard';

export default function App() {
	const [isLogIn, setLogIn] = useState(false);

	return <>{isLogIn ? <Dashboard /> : <LandingPage />}</>;
}
