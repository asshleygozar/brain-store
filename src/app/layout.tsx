import type { Metadata } from 'next';
import { Urbanist, Comfortaa, Inter } from 'next/font/google';

import './globals.css';

const urbanist = Urbanist({
	variable: '--font-urbanist',
	subsets: ['latin'],
});

const comforta = Comfortaa({
	variable: '--font-comforta',
	subsets: ['latin'],
});

const inter = Inter({
	variable: '--font-inter',
	subsets: ['latin'],
});

export const metadata: Metadata = {
	title: 'Blabber',
	description: 'Chat with your friends!',
};

export default function RootLayout({
	children,
}: Readonly<{
	children: React.ReactNode;
}>) {
	return (
		<html lang='en'>
			<body
				className={`${urbanist.variable} ${comforta.variable} ${inter.variable}`}
			>
				{children}
			</body>
		</html>
	);
}
