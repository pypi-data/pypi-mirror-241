//! The Gold language - a programmable configuration language inspired by Dhall.

#![feature(step_trait)]

#![warn(missing_docs)]

#[macro_use]
extern crate lazy_static;

/// This module defines the Gold Object type and all its variants.
#[macro_use]
pub mod object;

/// This module defines the type used as the error variant in all results.
pub mod error;

/// Types for the abstract syntax tree, the result of parsing.
mod ast;

/// Built-in Gold functions written in Rust rather than Gold.
mod builtins;

/// Core evaluation routines.
mod eval;

/// The Gold language lexer, which functions as input to the parser.
mod lexing;

/// The Gold language parser, which uses the output of the lexer to generate an AST.
mod parsing;

/// Utility traits.
mod traits;

/// Utility functions.
mod util;

#[cfg(test)]
mod tests;

/// This module defines Python bindings for the Gold language (but not the
/// actual module - see the goldpy crate).
#[cfg(feature = "python")]
pub mod python;

use std::fs::read_to_string;
use std::path::Path;

use eval::{eval as evaluate};
use error::{Error, FileSystem};

pub use object::Object;
pub use parsing::parse;
pub use eval::ImportConfig;


/// Evaluate Gold code and return the result.
///
/// Use `root` to define the root path for imports. If not given, relative path
/// imports will not be possible. Provide a custom import resolver for full
/// control over imports.
pub fn eval(input: &str, importer: &ImportConfig) -> Result<Object, Error> {
    let ret = parsing::parse(input).and_then(|file| evaluate(&file, importer));
    ret.map_err(|err| err.render(Some(input)))
}


/// Evaluate Gold code and return the result.
///
/// This is equivalent to calling [`eval`] with no path and an import resolver that always fails.
pub fn eval_raw(input: &str) -> Result<Object, Error> {
    eval(input, &ImportConfig::default())
}


/// Evaluate a Gold file and return the result.
///
/// This is equivalent to reading the file and calling [`eval`] with the source
/// code, the file's path and an import resolver that always fails. Relative
/// path imports will succeed.
pub fn eval_file(input: &Path) -> Result<Object, Error> {
    let contents = read_to_string(input).map_err(|_| Error::new(FileSystem::Read(input.to_owned())))?;
    let parent = input.parent().ok_or_else(|| Error::new(FileSystem::NoParent(input.to_owned())))?;
    eval(&contents, &ImportConfig::with_path(parent.to_owned()))
}
