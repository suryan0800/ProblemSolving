package com.tryout.project1;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import tutorial.Addressbook.AddressBook;
import com.tryout.project1.bo.AddPerson;
import com.tryout.project1.bo.ListPeople;

@SpringBootApplication
public class Project1Application implements CommandLineRunner {

	private static Logger LOG = LoggerFactory
			.getLogger(Project1Application.class);

	public static void main(String[] args) {
		SpringApplication.run(Project1Application.class, args);
	}

	@Override
	public void run(String... args) throws IOException {
		LOG.info("EXECUTING : command line runner");

		for (int i = 0; i < args.length; ++i) {
			LOG.info("args[{}]: {}", i, args[i]);
		}

		if (args.length != 2) {
			System.err.println("Usage:  AddPerson|ListPeople ADDRESS_BOOK_FILE");
			System.exit(-1);
		}

		if (args[0].equals("AddPerson")) {
			AddressBook.Builder addressBook = AddressBook.newBuilder();

			// Read the existing address book.
			try {
				addressBook.mergeFrom(new FileInputStream(args[1]));
			} catch (FileNotFoundException e) {
				System.out.println(args[0] + ": File not found.  Creating a new file.");
			}

			// Add an address.
			addressBook.addPeople(
					AddPerson.PromptForAddress(new BufferedReader(new InputStreamReader(System.in)),
							System.out));

			// Write the new address book back to disk.
			FileOutputStream output = new FileOutputStream(args[1]);
			addressBook.build().writeTo(output);
			output.close();
		} else if (args[0].equals("ListPeople")) {
			// Read the existing address book.
			AddressBook addressBook = AddressBook.parseFrom(new FileInputStream(args[1]));

			ListPeople.Print(addressBook);
		} else { 
			System.err.println("Unknown command");
		}
	}

}
