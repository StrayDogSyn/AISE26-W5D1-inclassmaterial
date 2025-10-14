# Lesson Materials

This directory contains presentation materials for the CI/CD workshop.

## Contents

### slides.pdf
Workshop presentation slides covering:
- Introduction to CI/CD concepts
- GitHub Actions basics
- Pipeline design
- Best practices
- Real-world examples

### CI/CD Pipeline Visualization

The workshop materials include a visual representation of the CI/CD pipeline flow:

```mermaid
graph TD
    A[Push Code] --> B[Lint]
    A --> C[Test]
    B --> D[Build]
    C --> D
    D --> E[Deploy Staging]
    E --> F{Manual Approval}
    F -->|Approved| G[Deploy Production]
    F -->|Rejected| H[End]
    G --> H
```

This diagram shows the complete pipeline stages from code push through production deployment.

