# Architecture

This document explains the general architecture of the DRDO DITCS Cybersecurity system.

The system is modular, with separate components for network management, audit management, policy enforcement, and cyber defense. Each module is responsible for its domain to ensure clear separation of concerns.

Modules communicate via centralized APIs. Security policies and configurations are maintained in the config directory.

Audit reports are generated and saved in the audit-reports folder.

The Flask framework serves as the main backend API.
