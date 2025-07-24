'use client';

import Link from 'next/link';
import { useState } from 'react';
import styles from '../page.module.css';
import { useRouter } from 'next/navigation';

export default function LogIn() {
	const router = useRouter();

	//For storing current input session
	const [username, setUsername] = useState('');
	const [password, setPassword] = useState('');

	//For span message immediate feeback
	const [usernameFeedback, setUsernameFeedback] = useState({
		feedback: '',
		isValid: true,
	});
	const [passwordFeedback, setPasswordFeedback] = useState({
		feedback: '',
		isValid: true,
	});

	//Function for form validation
	function handleSubmit(e: React.FormEvent<HTMLFormElement>) {
		//Prevent submission
		const preventDefault = () => {
			e.preventDefault();
			e.stopPropagation();
		};

		const usernameServer = 'asshley';
		const passwordServer = 'hello';
		//Username validation
		if (!username) {
			preventDefault();
			setUsernameFeedback((prev) => ({
				...prev,
				feedback: 'Please provide username',
				isValid: false,
			}));
			return;
		}

		//Password validation
		if (!password) {
			preventDefault();
			setPasswordFeedback((prev) => ({
				...prev,
				feedback: 'Please provide your password',
				isValid: false,
			}));
			return;
		}

		if (usernameServer !== username) {
			preventDefault();
			setUsernameFeedback((prev) => ({
				...prev,
				feedback: 'Invalid username',
				isValid: false,
			}));
			return;
		} else if (passwordServer !== password) {
			preventDefault();
			setPasswordFeedback((prev) => ({
				...prev,
				feedback: 'Invalid password',
				isValid: false,
			}));
			return;
		} else {
			router.replace('/dashboard');
		}
	}

	return (
		<form
			method='post'
			className={styles.form}
			onSubmit={handleSubmit}
		>
			<h1>Log In</h1>
			<label htmlFor='username'>
				Username{' '}
				<span
					className={usernameFeedback.isValid ? styles.valid : styles.invalid}
				>
					{usernameFeedback.feedback}
				</span>
				<input
					className={styles.logInFocus}
					id={'username'}
					type='text'
					placeholder='Enter username'
					required={true}
					value={username}
					onChange={(e) => setUsername(e.target.value)}
				/>
			</label>
			<label htmlFor='password'>
				Password{' '}
				<span
					className={passwordFeedback.isValid ? styles.valid : styles.invalid}
				>
					{passwordFeedback.feedback}
				</span>
				<input
					className={styles.logInFocus}
					id={'password'}
					type='password'
					placeholder='Enter password'
					required={true}
					value={password}
					onChange={(e) => setPassword(e.target.value)}
				/>
			</label>
			<button
				type='submit'
				className={styles.submitButton}
			>
				Log in
			</button>
			<p className={styles.navigateLink}>
				Don&lsquo;t have an account?
				<Link
					className={styles.link}
					href={'/auth/signup'}
				>
					{' '}
					Sign up{' '}
				</Link>
				instead
			</p>
		</form>
	);
}
