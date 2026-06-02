# Behavior-First Test Plan

A short plan for designing a test around observable behavior and stable interfaces. Pairs with the `testing` skill's **Behavior-first test design** and **Vertical test slice** modules.

## Behavior under test

_The capability the system should provide, stated as observable behavior._

## Public interface used

_The interface the test exercises (the seam a real caller would use)._

## User/system capability described

_What a passing test proves a user or caller can do._

## Why this test should survive refactoring

_Why the test stays valid if internal implementation changes but behavior does not._

## What would make it fail correctly

_The specific behavior gap that should turn the test red._

## Implementation coupling risks

_Where the test could accidentally couple to private methods, incidental data shape, or internal collaborators — and how it avoids that._

## Mocking rationale, if any

_What is mocked, why it is necessary, and why it does not lock the test to implementation. Leave empty if nothing is mocked._
