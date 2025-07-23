import type { Metadata } from "next";
import { Urbanist, Comfortaa } from "next/font/google";
import "./globals.css";

const urbanist = Urbanist({
  variable: "--font-urbanist",
  subsets: ["latin"],
});

const comforta = Comfortaa({
  variable: "--font-comforta",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "Blabber",
  description: "Chat with your friends!",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={`${urbanist.variable} ${comforta.variable}`}>
        {children}
      </body>
    </html>
  );
}
