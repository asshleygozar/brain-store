'use client';

import styles from '../page.module.css';
import Link from 'next/link';
import { useState } from 'react';

export default function SignUp() {
	// Username, Password, and Retype password states
	const [username, setUsername] = useState({
		username: '',
		feedback: '',
		isValid: false,
	});
	const [password, setPassword] = useState({
		password: '',
		reTypePassword: '',
	});

	//Password and retype password feedback
	const [passwordFeedback, setPasswordFeedback] = useState({
		passwordFeedback: '',
		isPasswordValid: false,
		matchFeedback: '',
		isMatch: false,
	});

	// Form feeback
	const [formFeedback, setFormFeedback] = useState('');

	// Handle username validation
	const handleUsername = (e: React.ChangeEvent<HTMLInputElement>) => {
		const value = e.target.value;

		setUsername((prev) => ({
			...prev,
			username: value,
		}));

		if (!value) {
			setUsername((prev) => ({
				...prev,
				feedback: 'Please provide a username',
				isValid: false,
			}));
		} else {
			setUsername((prev) => ({
				...prev,
				feedback: 'Cool name!',
				isValid: true,
			}));
		}
	};

	// Handle on match password change for live update feedback
	const handleMatchPassword = (e: React.ChangeEvent<HTMLInputElement>) => {
		const value = e.target.value;

		setPassword((prevRetypePassword) => ({
			...prevRetypePassword,
			reTypePassword: value,
		}));

		if (password.password !== value) {
			setPasswordFeedback((prevFeedback) => ({
				...prevFeedback,
				matchFeedback: 'Password does not match',
				isMatch: false,
			}));
		} else {
			setPasswordFeedback((prevFeedback) => ({
				...prevFeedback,
				matchFeedback: 'Password match!',
				isMatch: true,
			}));
		}
	};

	// Handle password validation live update
	const handlePasswordValidation = (e: React.ChangeEvent<HTMLInputElement>) => {
		const value = e.target.value;
		setPassword((prevPassword) => ({ ...prevPassword, password: value }));

		const passwordRegex =
			/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^\w\s]).{8,12}$/;

		if (!value) {
			setPasswordFeedback((prevFeedback) => ({
				...prevFeedback,
				passwordFeedback: 'Please provide password',
				isPasswordValid: false,
			}));
		} else if (value.length < 8) {
			setPasswordFeedback((prevFeedback) => ({
				...prevFeedback,
				passwordFeedback: 'Password must be at least 8 characters',
				isPasswordValid: false,
			}));
		} else if (!passwordRegex.test(value)) {
			setPasswordFeedback((prevFeedback) => ({
				...prevFeedback,
				passwordFeedback:
					'Password must include (lowercase, uppercase, special characters, and numbers)',
				isPasswordValid: false,
			}));
		} else {
			setPasswordFeedback((prevFeedback) => ({
				...prevFeedback,
				passwordFeedback: 'Great! Very strong.',
				isPasswordValid: true,
			}));
		}
	};

	// Handle submit || another layer form validation for security purposes
	const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
		const preventDefault = () => {
			e.preventDefault();
			e.stopPropagation();
		};
		if (!username.username.length) {
			preventDefault();
			setFormFeedback('Please provide the username with the requested format.');
		} else if (!password.password.length) {
			preventDefault();
			setFormFeedback(
				'Please provide the password with the requested characters'
			);
		} else if (password.password !== password.reTypePassword) {
			preventDefault();
			setFormFeedback('Password and Re-type password does not match');
		} else {
			setFormFeedback('Everything looks great!');
		}
	};

	return (
		<form
			method='post'
			className={styles.form}
			onSubmit={(e) => handleSubmit(e)}
		>
			<h1>Sign Up</h1>
			<div>
				<span>{formFeedback}</span>
			</div>
			<label htmlFor='username'>
				Username{' '}
				<span className={username.isValid ? styles.valid : styles.invalid}>
					{username.feedback}
				</span>
				<input
					className={username.isValid ? styles.inputValid : styles.inputInvalid}
					id='username'
					type='text'
					name='username'
					placeholder='Create username'
					value={username.username}
					onChange={(e) => handleUsername(e)}
				/>
			</label>
			<label htmlFor='password'>
				Password{' '}
				<span
					className={
						passwordFeedback.isPasswordValid ? styles.valid : styles.invalid
					}
				>
					{passwordFeedback.passwordFeedback}
				</span>
				<input
					className={
						passwordFeedback.isPasswordValid
							? styles.inputValid
							: styles.inputInvalid
					}
					id='password'
					type='password'
					name='password'
					placeholder='Minimum of 8 characters'
					pattern={'^(?=.*[a-z])(?=.*[A-Z])(?=.*d).{8,12}$'}
					value={password.password}
					onChange={(e) => handlePasswordValidation(e)}
				/>
			</label>
			<label htmlFor='re-type-password'>
				Re-type password{' '}
				<span
					className={passwordFeedback.isMatch ? styles.valid : styles.invalid}
				>
					{passwordFeedback.matchFeedback}
				</span>
				<input
					className={
						passwordFeedback.isMatch ? styles.inputValid : styles.inputInvalid
					}
					id='re-type-password'
					type='password'
					name='re-type-password'
					placeholder='Re type your password'
					value={password.reTypePassword}
					onChange={(e) => handleMatchPassword(e)}
				/>
			</label>
			<button
				type='submit'
				className={styles.submitButton}
			>
				Sign up
			</button>
			<p className={styles.navigateLink}>
				Already have an account?
				<Link
					href={'/auth/login'}
					className={styles.link}
				>
					{' '}
					Log In{' '}
				</Link>
				instead
			</p>
		</form>
	);
}
