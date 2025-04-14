#!/usr/bin/env Rscript

# Get command line arguments
args <- commandArgs(trailingOnly = TRUE)

if (length(args) != 3) {
  stop("Usage: Rscript r_wrapper.R <script_path> <output_dir> <output_file>")
}

script_path <- args[1]
output_dir <- args[2]
output_file <- args[3]

# Load necessary libraries
tryCatch({
  # Ensure required packages are installed and loaded
  required_packages <- c("ggplot2", "plotly", "rgl")
  for (pkg in required_packages) {
    if (!require(pkg, character.only = TRUE, quietly = TRUE)) {
      message(paste("Warning:", pkg, "package not available"))
    }
  }
}, error = function(e) {
  message("Error loading packages: ", e$message)
})

# Execute the user's script
tryCatch({
  # Set working directory to the output directory
  original_wd <- getwd()
  setwd(output_dir)
  # Create an environment for script execution
  script_env <- new.env()
  # Add variables to the environment
  script_env$output_dir <- output_dir
  script_env$output_file <- output_file
  # Source the script in the environment
  source(script_path, local = script_env)
  
  # Determine what kind of visualization we're dealing with and save it
  if (grepl("\\.html$", output_file)) {
    # For interactive or 3D visualizations
    if ("p" %in% ls(script_env) && "plotly" %in% loadedNamespaces()) {
      # Save Plotly visualization
      htmlwidgets::saveWidget(
        script_env$p, 
        file = file.path(output_dir, output_file),
        selfcontained = TRUE
      )
    } else if ("plot" %in% ls(script_env) && "plotly" %in% loadedNamespaces()) {
      # Alternative plotly object name
      htmlwidgets::saveWidget(
        script_env$plot, 
        file = file.path(output_dir, output_file),
        selfcontained = TRUE
      )
    } else if ("rgl" %in% loadedNamespaces()) {
      # Save RGL 3D visualization
      rgl::rglwidget() %>%
        htmlwidgets::saveWidget(
          file = file.path(output_dir, output_file),
          selfcontained = TRUE
        )
    } else {
      # Try to find any htmlwidget in the environment
      widget_found <- FALSE
      for (obj_name in ls(script_env)) {
        obj <- get(obj_name, script_env)
        if (inherits(obj, "htmlwidget")) {
          htmlwidgets::saveWidget(
            obj, 
            file = file.path(output_dir, output_file),
            selfcontained = TRUE
          )
          widget_found <- TRUE
          break
        }
      }

      if (!widget_found) {
        stop("No visualization object found to save as HTML")
      }
    }
  } else {
    # For static visualizations (PNG, PDF, etc.)
    if ("p" %in% ls(script_env) && (inherits(script_env$p, "gg") || inherits(script_env$p, "ggplot"))) {
      # Save ggplot2 visualization
      ggsave(
        file.path(output_dir, output_file),
        plot = script_env$p,
        width = 8,
        height = 6,
        dpi = 300
      )
    } else if ("plot" %in% ls(script_env) && (inherits(script_env$plot, "gg") || inherits(script_env$plot, "ggplot"))) {
      # Alternative ggplot object name
      ggsave(
        file.path(output_dir, output_file),
        plot = script_env$plot,
        width = 8,
        height = 6,
        dpi = 300
      )
    } else {
      # Save base R graphics
      if (exists("dev.cur") && dev.cur() > 1) {
        dev.copy(png, file.path(output_dir, output_file), width = 800, height = 600)
        dev.off()
      } else {
        png(file.path(output_dir, output_file), width = 800, height = 600)
        # Try to re-run any plotting function in the environment
        if ("plot_func" %in% ls(script_env) && is.function(script_env$plot_func)) {
          script_env$plot_func()
        }
        dev.off()
      }
    }
  }

  # Restore working directory
  setwd(original_wd)
  # Check if the output file was created
  if (file.exists(file.path(output_dir, output_file))) {
    message(paste("Visualization successfully saved to", file.path(output_dir, output_file)))
  } else {
    stop(paste("Output file", file.path(output_dir, output_file), "was not created"))
  }
}, error = function(e) {
  # Restore working directory in case of error
  if (exists("original_wd")) {
    setwd(original_wd)
  }
  
  message("Error executing script: ", e$message)
  quit(status = 1)
})